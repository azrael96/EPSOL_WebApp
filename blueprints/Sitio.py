#Import the necessary libraries
from flask import Blueprint, redirect, render_template, request, current_app
from flask_login import login_required, current_user

#generate the blueprint
sitioRutas = Blueprint('sitioRutas', __name__)

#define the routes of the blueprint
@sitioRutas.route("/AdminPlaces")
@login_required
def AdminPlaces():
    model = current_app.config["sitioModel"]
    places = model.getAllSites(current_user.user_client)
    return render_template("Sitio/AdministrarSitios.html", places=places)

@sitioRutas.route("/AddPlace")
@login_required
def AddPlace():
    return render_template("Sitio/IngresarSitio.html")

@sitioRutas.route("/SaveAddPlace", methods=["POST"])
@login_required
def SaveAddPlace():
    nombre = request.form["nombre"]
    ubicación = request.form["ubicación"]
    cliente = request.form["cliente"]

    model = current_app.config["sitioModel"]
    codigo = model.findMaxCodePlaces()
    model.addPlace(codigo, nombre, ubicación, cliente)
    return redirect("/AdminPlaces")

@sitioRutas.route("/DelPlace", methods=["POST"])
@login_required
def DelPlace():
    model = current_app.config["sitioModel"]
    model.delPlace(request.form["id"])
    return redirect("/AdminPlaces")

@sitioRutas.route("/UpdatePlace/<int:id>")
@login_required
def UpdatePlace(id):
    model = current_app.config["sitioModel"]
    place = model.searchPlace(id)
    return render_template("Sitio/EditarSitio.html", place=place)

@sitioRutas.route("/SaveUpdatePlace", methods=["POST"])
@login_required
def SaveUpdatePlace():
    id = request.form["id"]
    nombre = request.form["nombre"]
    ubicación = request.form["ubicación"]

    model = current_app.config["sitioModel"]
    model.updatePlace(id, nombre, ubicación)
    return redirect("/AdminPlaces")