from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape

app = Flask(__name__)


@app.get("/")
def raiz():
    return redirect(url_for("bienvenida"))


@app.get("/bienvenida")
def bienvenida():
    return render_template("bienvenida.html", nombre=nombre())


@app.get("/despedida")
def despedida():
    return render_template("despedida.html", nombre=nombre())


def nombre():
    return request.args.get("nombre", "Mundo")
