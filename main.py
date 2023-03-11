from flask import Flask, render_template, request, redirect, session, url_for
import connect as conn

app = Flask(__name__)
app.secret_key = '5e20e862a2afa65e8189e348cdfe7579c11a2e83'

if "__name__" == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    if 'Nick' in session:
        return redirect(url_for('GoDashboard'))
    else:
        return render_template('Login.html')

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = conn.searchLogin(username, password)
        if account:
            session['Nombre'] = account[0]
            session['Nick'] = account[3]
            session['Estado'] = 'En Linea'
            session['Tipo'] = account[1]
            session['Correo'] = account[2]
            session['Cliente'] = account[5]
            session['CodCli'] = account[6]
            return redirect(url_for('GoDashboard'))
        else:
            msg = 'Usuario/Contraseña Incorrecto!'
            return render_template('Login.html', msg=msg)

@app.route("/GoDashboard")
def GoDashboard():
    if 'Nick' in session:
        return render_template("Dashboard.html")
    else:
        return redirect(url_for('index'))

@app.route("/GoPerfil")
def GoPerfil():
    if 'Nick' in session:
        return render_template("Perfil.html")
    else:
        return redirect(url_for('index'))

@app.route("/GoMediciones")
def GoMediciones():
    if 'Nick' in session:
        mediciones = ((0, 0, 0),)
        return render_template("Mediciones.html", mediciones=mediciones)
    else:
        return redirect(url_for('index'))

@app.route("/AdminClients")
def AdminClients():
    if 'Nick' in session:
        clientes = conn.getAllClients()
        return render_template("AdministrarClientes.html", clientes=clientes)
    else:
        return redirect(url_for('index'))

@app.route("/AdminUsers")
def AdminUsers():
    if 'Nick' in session:
        users = conn.getAllUsers(session['CodCli'])
        return render_template("AdministrarUsuarios.html", users=users)
    else:
        return redirect(url_for('index'))

@app.route("/AdminPlaces")
def AdminPlaces():
    if 'Nick' in session:
        places = conn.getAllSites(session['CodCli'])
        return render_template("AdministrarSitios.html", places=places)
    else:
        return redirect(url_for('index'))

@app.route("/AdminAnalizers")
def AdminAnalizers():
    if 'Nick' in session:
        analizers = conn.getAllAnalizers()
        return render_template("AdministrarAnalizadores.html", analizers=analizers)
    else:
        return redirect(url_for('index'))

@app.route("/AddClient")
def AddClient():
    if 'Nick' in session:
        return render_template("IngresarCliente.html")
    else:
        return redirect(url_for('index'))

@app.route("/AddUser")
def AddUser():
    if 'Nick' in session:
        return render_template("IngresarUsuario.html")
    else:
        return redirect(url_for('index'))

@app.route("/AddPlace")
def AddPlace():
    if 'Nick' in session:
        return render_template("IngresarSitio.html")
    else:
        return redirect(url_for('index'))

@app.route("/AddAnalizer")
def AddAnalizer():
    if 'Nick' in session:
        return render_template("IngresarAnalizador.html")
    else:
        return redirect(url_for('index'))

@app.route("/SaveAddClient", methods=["POST"])
def SaveAddClient():
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    ciudad = request.form["ciudad"]
    estado = request.form["estado"]
    telefono = request.form["telefono"]
    suscripcion = request.form.get("suscripcion")
    pago = request.form.get("pago")
    cliente = conn.findMaxCodeClients()
    conn.addClient(cliente, nombre, suscripcion, pago, direccion, ciudad, estado, telefono)

    nombre = request.form["nombreUsu"]
    password = request.form["password"]
    tipo = request.form.get("tipo")
    correo = request.form["correo"]
    nick = request.form["nick"]
    conn.addUser(conn.findMaxCodeUsers(), nombre, password, tipo, correo, nick, cliente)

    return redirect("/AdminClients")

@app.route("/SaveAddUser", methods=["POST"])
def SaveAddUser():
    nombre = request.form["nombre"]
    password = request.form["password"]
    tipo = request.form.get("tipo")
    correo = request.form["correo"]
    nick = request.form["nick"]
    cliente = request.form["cliente"]
    conn.addUser(conn.findMaxCodeUsers(), nombre, password, tipo, correo, nick, cliente)
    return redirect("/AdminUsers")

@app.route("/SaveAddPlace", methods=["POST"])
def SaveAddPlace():
    nombre = request.form["nombre"]
    ubicación = request.form["ubicación"]
    cliente = request.form["cliente"]
    conn.addPlace(conn.findMaxCodePlaces(), nombre, ubicación, cliente)
    return redirect("/AdminPlaces")

@app.route("/SaveAddAnalizer", methods=["POST"])
def SaveAddAnalizer():
    fabricante = request.form["fabricante"]
    uso = request.form.get("uso")
    clase = request.form["clase"]
    conn.addAnalizer(conn.findMaxCodeAnalizer(), fabricante, uso, clase)
    return redirect("/AdminAnalizers")

@app.route("/DelClient", methods=["POST"])
def DelClient():
    conn.delClient(request.form["id"])
    return redirect("/AdminClients")

@app.route("/DelUser", methods=["POST"])
def DelUser():
    conn.delUser(request.form["id"])
    return redirect("/AdminUsers")

@app.route("/DelPlace", methods=["POST"])
def DelPlace():
    conn.delPlace(request.form["id"])
    return redirect("/AdminPlaces")

@app.route("/DelAnalizer", methods=["POST"])
def DelAnalizer():
    conn.delAnalizer(request.form["id"])
    return redirect("/AdminAnalizers")

@app.route("/UpdateClient/<int:id>")
def UpdateClient(id):
    client = conn.searchClient(id)
    return render_template("EditarCliente.html", client=client)

@app.route("/UpdateUser/<int:id>")
def UpdateUser(id):
    user = conn.searchUser(id)
    return render_template("EditarUsuario.html", user=user)

@app.route("/UpdatePlace/<int:id>")
def UpdatePlace(id):
    place = conn.searchPlace(id)
    return render_template("EditarSitio.html", place=place)

@app.route("/UpdateAnalizer/<int:id>")
def UpdateAnalizer(id):
    analizer = conn.searchAnalizer(id)
    return render_template("EditarAnalizador.html", analizer=analizer)

@app.route("/SaveUpdateClient", methods=["POST"])
def SaveUpdateClient():
    id = request.form["id"]
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    ciudad = request.form["ciudad"]
    estado = request.form["estado"]
    telefono = request.form["telefono"]
    suscripcion = request.form.get("suscripcion")
    pago = request.form.get("pago")
    conn.updateClient(id, nombre, direccion, ciudad, estado, telefono, suscripcion, pago)
    return redirect("/AdminClients")

@app.route("/SaveUpdateUser", methods=["POST"])
def SaveUpdateUser():
    id = request.form["id"]
    nombre = request.form["nombre"]
    password = request.form["password"]
    tipo = request.form["tipo"]
    correo = request.form["correo"]
    nick = request.form["nick"]

    conn.updateUser(id, nombre, password, tipo, correo, nick)
    return redirect("/AdminUsers")

@app.route("/SaveUpdatePlace", methods=["POST"])
def SaveUpdatePlace():
    id = request.form["id"]
    nombre = request.form["nombre"]
    ubicación = request.form["ubicación"]

    conn.updatePlace(id, nombre, ubicación)
    return redirect("/AdminPlaces")

@app.route("/SaveUpdateAnalizer", methods=["POST"])
def SaveUpdateAnalizer():
    id = request.form["id"]
    fabricante = request.form["fabricante"]
    uso = request.form.get("uso")
    clase = request.form["clase"]

    conn.updateAnalizer(id, fabricante, uso, clase)
    return redirect("/AdminAnalizers")

@app.route("/Logout")
def Logout():
    session.clear()
    return redirect(url_for('index'))