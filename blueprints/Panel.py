#Import the necessary libraries
from flask import render_template, request, redirect, session, url_for, Blueprint, current_app
from flask_login import login_required, login_user, current_user, logout_user

#generate the blueprint
panelRutas = Blueprint('panelRutas', __name__)

#define the routes of the blueprint
@panelRutas.route('/')
def StartPoint():
    if current_user.is_authenticated:
         return redirect(url_for('panelRutas.GoDashboard'))
    else:
         return render_template('Login.html')

@panelRutas.route('/Login', methods=['GET', 'POST'])
def Login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        model = current_app.config["usuarioModel"]
        user = model.checkUser(username, password)
        if user:
            login_user(user)
            return redirect(url_for('panelRutas.GoDashboard'))
        else:
            msg = 'Usuario/Contraseña Incorrecto!'
            return render_template('Login.html', msg=msg)

@panelRutas.route("/GoDashboard")
@login_required
def GoDashboard():
    return render_template("Dashboard.html")

@panelRutas.route("/GoPerfil")
@login_required
def GoPerfil():
    return render_template("Perfil.html")

@panelRutas.route("/Logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for('panelRutas.StartPoint'))