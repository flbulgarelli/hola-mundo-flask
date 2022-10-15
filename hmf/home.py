from flask import redirect, url_for

from hmf import app

@app.get("/")
def raiz():
    return redirect(url_for("bienvenida"))
