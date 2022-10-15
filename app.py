from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.get("/")
def hola_mundo():
    return  render_template( # 1
                "bienvenida.html", # 2
                nombre=request.args.get("nombre", "Mundo")) # 3
