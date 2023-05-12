#Import the necessary libraries
from flask import Blueprint, redirect, render_template, request, current_app
from flask_login import login_required

#generate the blueprint
medidorRutas = Blueprint('medidorRutas', __name__)

#define the routes of the blueprint
@medidorRutas.route("/AdminAnalizers")
@login_required
def AdminAnalizers():
    model = current_app.config["medidorModel"]
    analizers = model.getAllAnalizers()
    return render_template("Medidor/AdministrarAnalizadores.html", analizers=analizers)

@medidorRutas.route("/AddAnalizer")
@login_required
def AddAnalizer():
    return render_template("Medidor/IngresarAnalizador.html")

@medidorRutas.route("/SaveAddAnalizer", methods=["POST"])
@login_required
def SaveAddAnalizer():
    fabricante = request.form["fabricante"]
    uso_string = request.form.get("uso")
    clase = request.form["clase"]
    uso = True if uso_string == '1' else False

    model = current_app.config["medidorModel"]
    codigo = model.findMaxCodeAnalizer()
    model.addAnalizer(codigo, fabricante, uso, clase)
    return redirect("/AdminAnalizers")

@medidorRutas.route("/DelAnalizer", methods=["POST"])
@login_required
def DelAnalizer():
    model = current_app.config["medidorModel"]
    model.delAnalizer(request.form["id"])
    return redirect("/AdminAnalizers")

@medidorRutas.route("/UpdateAnalizer/<int:id>")
@login_required
def UpdateAnalizer(id):
    model = current_app.config["medidorModel"]
    analizer = model.searchAnalizer(id)
    return render_template("Medidor/EditarAnalizador.html", analizer=analizer)

@medidorRutas.route("/SaveUpdateAnalizer", methods=["POST"])
@login_required
def SaveUpdateAnalizer():
    id = request.form["id"]
    fabricante = request.form["fabricante"]
    uso_string = request.form.get("uso")
    clase = request.form["clase"]
    uso = True if uso_string == '1' else False

    model = current_app.config["medidorModel"]
    model.updateAnalizer(id, fabricante, uso, clase)
    return redirect("/AdminAnalizers")