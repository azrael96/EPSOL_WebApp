#Import the necessary libraries
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from models.Connector import Base
from models.Medicion import Measurement

#class that model the database table
class Dato(UserMixin, Base):
    __tablename__ = "measurements"

    timestamp = Column(Integer, primary_key=True)
    powerFactor = Column(String(50))
    thd = Column(String(50))
    measure_meas = Column(Integer, ForeignKey(Measurement.id))

    id = synonym("class_name")
    def __repr__(self):
        return '<Dato %r>' % self.timestamp

#class that manipulates the model
class datoModel:
    def __init__(self, db):
        self.db = db

    def getThdpromData(self, codigo):
        table = Dato
        filterA = Dato.measure_meas == codigo
        query = self.db.session.query(table.timestamp, table.thd).filter(filterA).all()
        return query

    def getPowerFactorData(self, codigo):
        table = Dato
        filterA = Dato.measure_meas == codigo
        query = self.db.session.query(table.timestamp, table.powerFactor).filter(filterA).all()
        return query