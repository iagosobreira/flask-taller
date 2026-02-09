from flask import Blueprint, render_template

main=Blueprint("main", __name__)

@main.route("/")
def inicio():
    return render_template("index.html")

@main.route("/login")
def inicio_login():
    return render_template("login.html")

@main.route("/registro")
def inicio_registro():
    return render_template("registro.html")