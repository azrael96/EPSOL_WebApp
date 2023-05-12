#Import the necessary libraries
from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary, Text
from sqlalchemy.orm import synonym, relationship
from sqlalchemy.sql.expression import func

#Conect with the necessary internal components
from models.Cliente import Clients
from models.Connector import Base

#class that model the database table
class Users(UserMixin, Base):
    __tablename__ = "users"
    user_ID = Column(Integer, primary_key=True)
    user_name = Column(String(50))
    user_pass = Column(LargeBinary)
    user_type = Column(String(50))
    email  = Column(String(50))
    user_client = Column(Integer, ForeignKey(Clients.id))
    nick  = Column(String(20))

    id = synonym("user_ID")
    cliente = relationship('Clients', foreign_keys='Users.user_client')
    def __repr__(self):
        return '<User %r>' % self.nick

#class that manipulates the model
class usuarioModel:
    def __init__(self, db):
        self.db = db

    def checkUser(self, username, password):
        table = Users
        filterA = Users.nick==username
        #filterB = Users.user_pass==password

        query = self.db.session.query(table).filter(filterA).first()
        if query != None:
            bc = current_app.config["bcrypt"]
            data = query.user_pass
            print(data, type(data))

            hash = bytes(data)
            print(hash, type(hash))

            print(type(query.user_pass), type(hash))

            flag = bc.check_password_hash(hash, password)
            print (bc.check_password_hash(hash, password))

            if flag:
                return query
            else:
                return None
        else:
            return None

    def getAllUsers(self, codigo):
        table = Users.__table__.columns
        filterA = Users.user_client == codigo
        filterB = Users.user_ID != 200000
        query = self.db.session.query(table).filter(filterA, filterB).all()
        return query

    def findMaxCodeUsers(self):
        table = Users
        filter = func.max(table.user_ID)
        query = self.db.session.query(filter).first()
        if query[0] == None:
            return 200001
        else:
            return int(query[0]) + 1

    def searchUser(self, codigo):
        table = Users.__table__.columns
        filter = Users.user_ID == codigo
        query = self.db.session.query(table).filter(filter).first()
        return query

    def addUser(self, Cod, Nom, Pwd, Tip, Cor, Nic, Cli):

        bc = current_app.config["bcrypt"]
        passBC = bc.generate_password_hash(Pwd)

        new_rec = Users(user_ID=Cod, user_name=Nom, user_pass=passBC,
                        user_type=Tip, email=Cor, nick=Nic, user_client=Cli)
        self.db.session.add(new_rec)
        self.db.session.commit()

    def updateUser(self, Cod, Nom, Pas, Tip, Cor, Nic):
        table = Users
        filter = Users.user_ID == Cod

        bc = current_app.config["bcrypt"]
        passBC = bc.generate_password_hash(Pas)

        updated_rec = self.db.session.query(table).filter(filter).first()
        updated_rec.user_name = Nom
        updated_rec.user_pass = passBC
        updated_rec.user_type = Tip
        updated_rec.email = Cor
        updated_rec.nick = Nic

        self.db.session.commit()

    def delUser(self, cod):
        table = Users
        filter = Users.user_ID == cod

        deleted_rec = self.db.session.query(table).filter(filter).first()
        self.db.session.delete(deleted_rec)
        self.db.session.commit()

    def delClient(self, cod):
        table = Users
        filter = Users.user_client == cod

        deleted_rec = self.db.session.query(table).filter(filter).all()
        for instance in deleted_rec:
            self.db.session.delete(instance)

        self.db.session.commit()