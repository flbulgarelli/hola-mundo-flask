from flask import redirect, render_template

from hmf import app

@app.get("/")
def home():
    return render_template("home.html")
