from flask import Flask, render_template, request, redirect, session
import connect as conn

app = Flask(__name__)
app.secret_key = 'secretkey'

if "__name__" == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template("Login.html")

@app.route('/Login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = conn.searchLogin(username, password)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return render_template('Dashboard.html')
        else:

            msg = 'Usuario/Contraseña Incorrecto!'
            return render_template('Login.html', msg=msg)

@app.route("/GoDashboard")
def GoDashboard():
    return render_template("Dashboard.html")

@app.route("/GoPerfil")
def GoPerfil():
    return render_template("Perfil.html")

@app.route("/GoMediciones")
def GoMediciones():
    mediciones = ((0, 0, 0), )
    return render_template("Mediciones.html", mediciones=mediciones)

@app.route("/AdminClients")
def AdminClients():
    clientes = conn.getAllClients()
    return render_template("AdministrarClientes.html", clientes=clientes)

@app.route("/AdminUsers")
def AdminUsers():
    users = conn.getAllUsers()
    return render_template("AdministrarUsuarios.html", users=users)

@app.route("/AdminPlaces")
def AdminPlaces():
    places = conn.getAllSites()
    return render_template("AdministrarSitios.html", places=places)

@app.route("/AdminAnalizers")
def AdminAnalizers():
    analizers = conn.getAllAnalizers()
    return render_template("AdministrarAnalizadores.html", analizers=analizers)

@app.route("/AddClient")
def AddClient():
    return render_template("IngresarCliente.html")

@app.route("/AddUser")
def AddUser():
    return render_template("IngresarUsuario.html")

@app.route("/AddPlace")
def AddPlace():
    return render_template("IngresarSitio.html")

@app.route("/AddAnalizer")
def AddAnalizer():
    return render_template("IngresarAnalizador.html")

@app.route("/SaveAddClient", methods=["POST"])
def SaveAddClient():
    nombre = request.form["nombre"]
    direccion = request.form["direccion"]
    ciudad = request.form["ciudad"]
    estado = request.form["estado"]
    telefono = request.form["telefono"]
    conn.addClient(conn.findMaxCodeClients(), nombre, 1, 1, direccion, ciudad, estado, telefono)
    return redirect("/AdminClients")

@app.route("/SaveAddUser", methods=["POST"])
def SaveAddUser():
    nombre = request.form["nombre"]
    password = request.form["password"]
    tipo = request.form["tipo"]
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
    if uso == None:
        uso = 0
    else:
        uso = 1
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

    conn.updateClient(id, nombre, direccion, ciudad, estado, telefono)
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
    if uso == None:
        uso = 0
    else:
        uso = 1
    clase = request.form["clase"]

    conn.updateAnalizer(id, fabricante, uso, clase)
    return redirect("/AdminAnalizers")