#Import the necessary libraries
from flask import Blueprint, redirect, render_template, request, current_app
from flask_login import login_required, current_user

#generate the blueprint
usuarioRutas = Blueprint('usuarioRutas', __name__)

#define the routes of the blueprint
@usuarioRutas.route("/AdminUsers")
@login_required
def AdminUsers():
    model = current_app.config["usuarioModel"]
    users = model.getAllUsers(current_user.user_client)
    return render_template("Usuario/AdministrarUsuarios.html", users=users)

@usuarioRutas.route("/AddUser")
@login_required
def AddUser():
    return render_template("Usuario/IngresarUsuario.html")

@usuarioRutas.route("/SaveAddUser", methods=["POST"])
@login_required
def SaveAddUser():
    nombre = request.form["nombre"]
    password = request.form["password"]
    tipo = request.form.get("tipo")
    correo = request.form["correo"]
    nick = request.form["nick"]
    cliente = request.form["cliente"]

    model = current_app.config["usuarioModel"]
    codigo = model.findMaxCodeUsers()
    model.addUser(codigo, nombre, password, tipo, correo, nick, cliente)
    return redirect("/AdminUsers")

@usuarioRutas.route("/DelUser", methods=["POST"])
@login_required
def DelUser():
    model = current_app.config["usuarioModel"]
    model.delUser(request.form["id"])
    return redirect("/AdminUsers")

@usuarioRutas.route("/UpdateUser/<int:id>")
@login_required
def UpdateUser(id):
    model = current_app.config["usuarioModel"]
    user = model.searchUser(id)
    return render_template("Usuario/EditarUsuario.html", user=user)

@usuarioRutas.route("/SaveUpdateUser", methods=["POST"])
@login_required
def SaveUpdateUser():
    id = request.form["id"]
    nombre = request.form["nombre"]
    password = request.form["password"]
    tipo = request.form["tipo"]
    correo = request.form["correo"]
    nick = request.form["nick"]

    model = current_app.config["usuarioModel"]
    model.updateUser(id, nombre, password, tipo, correo, nick)
    return redirect("/AdminUsers")