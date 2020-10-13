from flask import Flask, render_template, url_for, abort, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from aplicacion import config
from aplicacion.forms import formLogin, formRegister, formEnsureDelete
from aplicacion import avatar
from flask_socketio import SocketIO, send
#Flask Login
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.config.from_object(config)
socketio = SocketIO(app)
db = SQLAlchemy(app)

# Controlador con Flask_Login
# Necesarios unos métodos en models.py (Usuarios)
# para su control
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Si un user no tiene permiso de acceso a una ruta, es redirigido a login

#########################################
## LOS MODELOS LOS CARGAMOS DESPÚES    ##
## DE INSTANCIAR LA BASE DA DATOS 'db' ##
#########################################

from aplicacion.models import Usuarios

@login_manager.user_loader  # Se le pasa un objeto Usuario
def load_user(user_id):     # detecta automaticamente su campo 'id'
    '''
        Indica a Flask_Login como obtener
        el usuario actual mediante su id.
        Se inicializa como 'current_user'.
    '''
    return Usuarios.query.get(int(user_id))


# ACUERDATE QUE HAS INICIADO EL MANAGER CON SOCKET.RUN()!!
# CAMBIALO SI NO LOS VAS A USAR

@app.route('/')
def inicio():
    initScore = 0
    if current_user.is_authenticated:
        initScore = Usuarios.query.get(current_user.get_id()).score

    topUsers = Usuarios.query.order_by(desc('score')).limit(3)
    return render_template('inicio.html', rankin=topUsers, initScore=initScore)


@app.route('/score/<id>/<score>', methods=["POST", "GET"])   # No es seguro enviarlo desde un href...
@login_required                     # muy vulnerable (enviar por post)
def update_score(id, score):
    user = Usuarios.query.get(id)
    if user is None:
        abort(404)

    newScore = 0
    try:
        newScore = int(score)
    except:
        abort(404)

    user.score = newScore
    db.session.commit()
    return redirect(url_for("inicio"))



####### SOCKETS TESTING ##########

# Necesario lanzar el manager con socket.run
#@app.route("/sockets")
#def sockets_test():
#    return render_template("sockets_test.html")


#@socketio.on('message')
#def handleMessage(msg):
#    print("MSG --- > " + msg)
#    send(msg, broadcast=True)


@app.route('/rankin_mundial')
def rankin_mundial():
    users = Usuarios.query.order_by(desc('score')).all()
    return render_template('rankin_mundial.html', users=users)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    form = formLogin()

    if form.validate_on_submit():
        #POST
        user = Usuarios.query.filter_by(username=form.username.data).first()
        if user != None and user.verify_password(form.password.data): # Lamamos al método del objeto user
            login_user(user)    # Logeamos al usuario con flask login, para acceder a el como current_user
            return redirect(url_for("inicio"))
        form.username.errors.append("Datos usuario y contraseña incorrectos")

    return render_template("login.html", form=form)



@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    # cargamos las opciones de los radiobuttons (avatar)
    form = formRegister()
    available_avatars = avatar.getRangeAvatars("Novato")
    form.avatar.choices = available_avatars

    if form.validate_on_submit():
        #POST
        # Comprobamos que el username no existe
        username_exist = Usuarios.query.filter_by(username=form.username.data).first()
        if username_exist == None:
            user = Usuarios()
            form.populate_obj(user)
            user.admin = False
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('inicio'))
        form.username.errors.append("Nombre de usuario pillado, te jodes.")
    return render_template("register.html", form=form)


@app.route("/user/<id>/delete", methods=["GET", "POST"])
@login_required
def delete_user(id):
    if not current_user.is_admin():
        abort(404)

    user = Usuarios.query.get(id)
    if user is None:
        abort(404)

    form = formEnsureDelete()
    if form.validate_on_submit():
        #POST
        if form.yes.data:   # Si aceptamos borrar...
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for("rankin_mundial"))
    return render_template("ensureAction.html", form=form, user=user)


@app.route("/user/<id>/edit", methods=["GET", "POST"])
@login_required
def edit_user(id):
    pass



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("inicio"))


@app.route("/uncoming")
def cookies_terms():
    return render_template("uncoming.html")



@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error="Página no encontrada . . ."), 404
