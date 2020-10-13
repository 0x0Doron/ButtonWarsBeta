from flask_script import Manager
from aplicacion.app import app, db, socketio
from aplicacion.models import *
from getpass import getpass


manager = Manager(app)
app.config['DEBUG'] = True

@manager.command
def create_tables():
    db.create_all()

@manager.command
def drop_tables():
    db.drop_all()

@manager.command
def add_data_tables():
    '''Para añadir usuarios de prueba'''
    db.create_all()

    usuarios = [
        {"username":"SuperCalimero32", "password_hash":"password", "avatar":"default_avatar.png", "warcry":"hey mama!"},
        {"username":"Simmon12", "password_hash":"password", "avatar":"default_avatar.png", "warcry":"hey mama!"},
        {"username":"AmbrosseAsno", "password_hash":"password", "avatar":"default_avatar.png", "warcry":"hey mama!"},
        {"username":"Elodin9281398", "password_hash":"password", "avatar":"default_avatar.png", "warcry":"hey mama!"},
        {"username":"Auri2Vg", "password_hash":"password", "avatar":"default_avatar.png", "warcry":"hey mama!"}
    ]

    for use in usuarios:
        usuario = Usuarios(**use)
        db.session.add(usuario)
        db.session.commit()

@manager.command
def create_admin():
    usuario = {
        "username":input("Username: "),
        "password":getpass("Password: "),
        "avatar":"admin.png",
        "warcry":"Bollocks!",
        "range":"Zeus",
        "admin":True
    }
    nuevoUsuario = Usuarios(**usuario)
    db.session.add(nuevoUsuario)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
