#Import the necessary libraries
from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from models.Medidor import Analizers
from models.Sitio import Sites
from models.Connector import Base

#class that model the database table
class Measurement(UserMixin, Base):
    __tablename__ = "mestables"

    meas_ID = Column(Integer, primary_key=True)
    meas_site = Column(Integer, ForeignKey(Sites.id))
    meas_analizer = Column(Integer, ForeignKey(Analizers.id))

    id = synonym("meas_ID")
    def __repr__(self):
        return '<Medicion %r>' % self.meas_ID

#class that manipulates the model
class medicionModel:
    def __init__(self, db):
        self.db = db
