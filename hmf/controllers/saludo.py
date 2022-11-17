from flask import request, render_template
from datetime import datetime
from hmf import app

saludos_recientes = []

@app.get("/bienvenida")
def bienvenida():
    quien = nombre()
    saludos_recientes.append({'nombre': quien, 'fecha': datetime.now()})

    return render_template("bienvenida.html", nombre=quien)


@app.get("/despedida")
def despedida():
    return render_template("despedida.html", nombre=nombre())

@app.get("/recientes")
def recientes():
    return render_template("recientes.html", recientes=saludos_recientes)

def nombre():
    return request.args.get("nombre", "Mundo")
