from flask import request, render_template
from hmf import app, saludos
from datetime import datetime
import timeago

@app.get("/bienvenida")
def bienvenida():
    quien = nombre()
    saludos.registrar_saludo(quien, request.remote_addr)
    return render_template("bienvenida.html", nombre=quien)

@app.get("/despedida")
def despedida():
    return render_template("despedida.html", nombre=nombre())

@app.get("/recientes")
def recientes():
    return render_template("recientes.html", recientes=saludos.recientes, formatear_fecha=formatear_fecha)

def nombre():
    return request.args.get("nombre", "Mundo")


def formatear_fecha(fecha):
    return timeago.format(fecha, datetime.now(), 'es')