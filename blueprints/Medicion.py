#Import the necessary libraries
from flask import Blueprint, render_template, make_response, current_app
from flask_login import login_required

#Conect with the necessary internal components
from models import graphs as graphs

#generate the blueprint
medicionRutas = Blueprint('medicionRutas', __name__)

#define the routes of the blueprint
@medicionRutas.route("/GoMediciones")
@login_required
def GoMediciones():
    return render_template("Medicion/Mediciones.html")

@medicionRutas.route("/Gothdprom")
@login_required
def Gothdprom():
    return render_template("Medicion/thdprom.html")

@medicionRutas.route("/Gopft3")
@login_required
def Gopft3():
    return render_template("Medicion/pft3.html")

@medicionRutas.route('/thdprom')
@login_required
def thdprom():
    model = current_app.config["datoModel"]
    resp = make_response(graphs.giveGraph(model.getThdpromData(9000)))
    resp.mimetype = 'application/json'
    return resp

@medicionRutas.route('/pft3')
@login_required
def pft3():
    model = current_app.config["datoModel"]
    resp = make_response(graphs.giveGraph(model.getPowerFactorData(9000)))
    resp.mimetype = 'application/json'
    return resp