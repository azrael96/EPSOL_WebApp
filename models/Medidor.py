#Import the necessary libraries
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from models.Connector import Base

#class that model the database table
class Analizers(UserMixin, Base):
    __tablename__ = "analizers"

    analizer_ID = Column(Integer, primary_key=True)
    manufacturer_name = Column(String(50))
    usage_flag = Column(Boolean)
    class_name  = Column(String(50))

    id = synonym("class_name")
    def __repr__(self):
        return '<Medidor %r>' % self.analizer_ID

#class that manipulates the model
class medidorModel:
    def __init__(self, db):
        self.db = db

    def findMaxCodeAnalizer(self):
        table = Analizers
        filter = func.max(table.analizer_ID)
        query = self.db.session.query(filter).first()
        if query[0] == None:
            return 400001
        else:
            return int(query[0]) + 1

    def getAllAnalizers(self):
        table = Analizers.__table__.columns
        query = self.db.session.query(table).all()
        return query

    def searchAnalizer(self, codigo):
        table = Analizers.__table__.columns
        filter = Analizers.analizer_ID == codigo
        query = self.db.session.query(table).filter(filter).first()
        return query

    def addAnalizer(self, Cod, Fab, Use, Cla):
        new_rec = Analizers(analizer_ID=Cod, manufacturer_name=Fab, usage_flag=Use,
                        class_name=Cla)
        self.db.session.add(new_rec)
        self.db.session.commit()

    def updateAnalizer(self, Cod, Fab, Uso, Cla):
        table = Analizers
        filter = Analizers.analizer_ID == Cod

        updated_rec = self.db.session.query(table).filter(filter).first()
        updated_rec.manufacturer_name = Fab
        updated_rec.usage_flag = Uso
        updated_rec.class_name = Cla
        self.db.session.commit()

    def delAnalizer(self, cod):
        table = Analizers
        filter = Analizers.analizer_ID == cod

        deleted_rec = self.db.session.query(table).filter(filter).first()
        self.db.session.delete(deleted_rec)
        self.db.session.commit()
