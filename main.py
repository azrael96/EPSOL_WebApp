#Import the necessary libraries
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

#Conect with the necessary internal components
from blueprints.Panel import panelRutas
from blueprints.Cliente import clienteRutas
from blueprints.Medicion import medicionRutas
from blueprints.Medidor import medidorRutas
from blueprints.Sitio import sitioRutas
from blueprints.Usuario import usuarioRutas
from models.Cliente import clienteModel
from models.Medidor import medidorModel
from models.Sitio import sitioModel
from models.Dato import datoModel
from models.Usuario import Users, usuarioModel
from models.Connector import connection_string

#Initialize principal app
app = Flask(__name__)
app.secret_key = '5e20e862a2afa65e8189e348cdfe7579c11a2e83'
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

#Define the main components of the app
login_manager = LoginManager()
bcrypt = Bcrypt()
db = SQLAlchemy()

#Initialize the main components of the app
login_manager.init_app(app)
bcrypt.init_app(app)
db.init_app(app)

#Import the routes to the app
app.register_blueprint(panelRutas)
app.register_blueprint(clienteRutas)
app.register_blueprint(usuarioRutas)
app.register_blueprint(sitioRutas)
app.register_blueprint(medidorRutas)
app.register_blueprint(medicionRutas)

#generate the models to be used
app.config["usuarioModel"] = usuarioModel(db)
app.config["sitioModel"] = sitioModel(db)
app.config["medidorModel"] = medidorModel(db)
app.config["clienteModel"] = clienteModel(db)
app.config["datoModel"] = datoModel(db)
app.config["bcrypt"] = bcrypt

#test enviorment
'''
with app.app_context():
    datoModel = datoModel(db)
    print(datoModel.getThdpromData(9000))
    print(datoModel.getPowerFactorData(9000))
'''

#Start the app
if "__name__" == "__main__":
    app.run(debug=True)

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(int(user_id))
