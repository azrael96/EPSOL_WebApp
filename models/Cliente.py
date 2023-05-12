#Import the necessary libraries
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from models.Connector import Base

#class that model the database table
class Clients(UserMixin, Base):
    __tablename__ = "clients"
    client_ID = Column(Integer, primary_key=True)
    client_name = Column(String(50))
    subscription_flag = Column(Boolean)
    payment_flag = Column(Boolean)
    client_address = Column(String(50))
    client_city = Column(String(50))
    client_state = Column(String(50))
    client_phone = Column(String(11))
    id = synonym("client_ID")
    def __repr__(self):
        return '<Cliente %r>' % self.client_name

#class that manipulates the model
class clienteModel:
    def __init__(self, db):
        self.db = db

    def getAllClients(self):
        table = Clients.__table__.columns
        filter = Clients.client_ID != 100000
        query = self.db.session.query(table).filter(filter).all()
        print(query)
        return query

    def findMaxCodeClients(self):
        table = Clients
        filter = func.max(table.client_ID)
        query = self.db.session.query(filter).first()
        if query[0] == None:
            return 100001
        else:
            return int(query[0]) + 1

    def searchClient(self, codigo):
        table = Clients.__table__.columns
        filter = Clients.client_ID == codigo
        query = self.db.session.query(table).filter(filter).first()
        return query

    def addClient(self, Cod, Nom, Pay, Sus, Dir, Ciu, Est, Tel):
        new_rec = Clients(client_ID=Cod, client_name=Nom, subscription_flag=Pay,
                          payment_flag=Sus, client_address=Dir, client_city=Ciu,
                          client_state=Est, client_phone=Tel)
        self.db.session.add(new_rec)
        self.db.session.commit()

    def updateClient(self, Cod, Nom, Dir, Ciu, Est, Tel, Sus, Pay):
        table = Clients
        filter = Clients.client_ID == Cod

        updated_rec = self.db.session.query(table).filter(filter).first()
        updated_rec.client_name = Nom
        updated_rec.subscription_flag = Pay
        updated_rec.payment_flag = Sus
        updated_rec.client_address = Dir
        updated_rec.client_city = Ciu
        updated_rec.client_state = Est
        updated_rec.client_phone = Tel

        self.db.session.commit()

    def delClient(self, cod):
        table = Clients
        filter = Clients.client_ID == cod

        deleted_rec = self.db.session.query(table).filter(filter).first()
        self.db.session.delete(deleted_rec)
        self.db.session.commit()

