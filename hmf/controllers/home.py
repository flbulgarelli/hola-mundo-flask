from flask import redirect, render_template, url_for

from hmf import app

@app.get("/")
def home():
    return render_template("home.html")

# Esta ruta es totalmente opcional
# Y a fines de demostración de redirect
@app.get("/home")
def home_alias():
    return redirect(url_for("home"))
