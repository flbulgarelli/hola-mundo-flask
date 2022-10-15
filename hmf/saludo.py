from flask import request, render_template

from hmf import app

@app.get("/bienvenida")
def bienvenida():
    return render_template("bienvenida.html", nombre=nombre())


@app.get("/despedida")
def despedida():
    return render_template("despedida.html", nombre=nombre())


def nombre():
    return request.args.get("nombre", "Mundo")
