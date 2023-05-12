#Import the necessary libraries
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import synonym

#Conect with the necessary internal components
from models.Cliente import Clients
from models.Connector import Base

#class that model the database table
class Sites(UserMixin, Base):
    __tablename__ = "sites"

    site_ID = Column(Integer, primary_key=True)
    site_name = Column(String(50))
    site_location = Column(String(50))
    site_client = Column(Integer, ForeignKey(Clients.id))

    id = synonym("site_ID")
    def __repr__(self):
        return '<Sitio %r>' % self.site_name

#class that manipulates the model
class sitioModel:
    def __init__(self, db):
        self.db = db
    def getAllSites(self, codigo):
        table = Sites.__table__.columns
        filter = Sites.site_client == codigo
        query = self.db.session.query(table).filter(filter).all()
        return query

    def findMaxCodePlaces(self):
        table = Sites
        filter = func.max(table.site_ID)
        query = self.db.session.query(filter).first()
        if query[0] == None:
            return 300001
        else:
            return int(query[0]) + 1

    def searchPlace(self, codigo):
        table = Sites.__table__.columns
        filter = Sites.site_ID == codigo
        query = self.db.session.query(table).filter(filter).first()
        return query

    def addPlace(self, Cod, Nom, Ubi, Cli):
        new_rec = Sites(site_ID=Cod, site_name=Nom, site_location=Ubi,
                        site_client=Cli)
        self.db.session.add(new_rec)
        self.db.session.commit()

    def updatePlace(self, Cod, Nom, Loc):
        table = Sites
        filter = Sites.site_ID == Cod

        updated_rec = self.db.session.query(table).filter(filter).first()
        updated_rec.site_name = Nom
        updated_rec.site_location = Loc

        self.db.session.commit()

    def delPlace(self, cod):
        table = Sites
        filter = Sites.site_ID == cod

        deleted_rec = self.db.session.query(table).filter(filter).first()
        self.db.session.delete(deleted_rec)
        self.db.session.commit()