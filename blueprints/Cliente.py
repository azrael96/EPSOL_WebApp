#Import the necessary libraries
from flask import Blueprint, redirect, render_template, request, current_app
from flask_login import login_required

#generate the blueprint
clienteRutas = Blueprint('clienteRutas', __name__)

#define the routes of the blueprint
@clienteRutas.route("/AdminClients")
@login_required
def AdminClients():
    model = current_app.config["clienteModel"]
    clientes = model.getAllClients()
    return render_template("Cliente/AdministrarClientes.html", clientes=clientes)

@clienteRutas.route("/AddClient")
@login_required
def AddClient():
    return render_template("Cliente/IngresarCliente.html")

@clienteRutas.route("/SaveAddClient", methods=["POST"])
@login_required
def SaveAddClient():
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    ciudad = request.form["ciudad"]
    estado = request.form["estado"]
    telefono = request.form["telefono"]
    sus_string = request.form.get("suscripcion")
    pago_string = request.form.get("pago")

    suscripcion = True if sus_string == '1' else False
    pago = True if pago_string == '1' else False

    model = current_app.config["clienteModel"]
    cliente = model.findMaxCodeClients()
    model.addClient(cliente, nombre, suscripcion, pago, direccion, ciudad, estado, telefono)

    nombre = request.form["nombreUsu"]
    password = request.form["password"]
    tipo = request.form.get("tipo")
    correo = request.form["correo"]
    nick = request.form["nick"]

    modelU = current_app.config["usuarioModel"]
    codigo = modelU.findMaxCodeUsers()
    modelU.addUser(codigo, nombre, password, tipo, correo, nick, cliente)

    return redirect("/AdminClients")

@clienteRutas.route("/DelClient", methods=["POST"])
@login_required
def DelClient():
    modelU = current_app.config["usuarioModel"]
    modelU.delClient(request.form["id"])

    model = current_app.config["clienteModel"]
    model.delClient(request.form["id"])

    return redirect("/AdminClients")
@clienteRutas.route("/UpdateClient/<int:id>")
@login_required
def UpdateClient(id):
    model = current_app.config["clienteModel"]
    client = model.searchClient(id)
    return render_template("Cliente/EditarCliente.html", client=client)

@clienteRutas.route("/SaveUpdateClient", methods=["POST"])
@login_required
def SaveUpdateClient():
    id = request.form["id"]
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    ciudad = request.form["ciudad"]
    estado = request.form["estado"]
    telefono = request.form["telefono"]
    sus_string = request.form.get("suscripcion")
    pago_string = request.form.get("pago")

    suscripcion = True if sus_string == '1' else False
    pago = True if pago_string == '1' else False

    model = current_app.config["clienteModel"]
    model.updateClient(id, nombre, direccion, ciudad, estado, telefono, suscripcion, pago)
    return redirect("/AdminClients")

