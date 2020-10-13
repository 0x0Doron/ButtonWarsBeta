# Almacenaremos las cookies en formato json
#   datos = [{"score":233333, "id":23}, {"score":233333, "id":23}, {"score":233333, "id":23}]

from flask import Flask, request, redirect
import time

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Estas en el inicio"


@app.route("/set_cookie")
def set_cookie():
    hora = str(time.time())
    redirect_to_index = redirect("/")
    response = app.make_response(redirect_to_index)
    response.set_cookie("cookie_time", value=hora)
    return response


@app.route("/get_cookie")
def get_cookie():
    datos = request.cookies.get("cookie_time")
    if datos != None:
        return datos
    else:
        return "Lo lamento, no hay ninguna cookie"


@app.route("/del_cookie")
def del_cookie():
    redirect_to_index = redirect("/")
    response = app.make_response(redirect_to_index)
    response.set_cookie("cookie_time", value="", expires=0)
    return response # Expires 0 borra la cookie del cliente


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True)
