import mysql.connector

class DatabaseLink():
    def __init__(self):
        self.cursor = ""
        self.state = ""
        self.database = ""

    def connect(self):
        try:
            self.database = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="safe&SOUND96",
                database="epsol_bd"
            )
            self.cursor = self.database.cursor()
            self.state = "Conectado al servidor correctamente"
        except:
            self.state = "No esta conectado al servidor"
    def disconect(self):
        self.database.close()
    def findMaxCodeClients(self):
        self.connect()
        query = "SELECT MAX(client_ID) FROM clients"
        self.cursor.execute(query)
        cod = self.cursor.fetchone()
        self.disconect()
        if cod[0] == None:
            return 100001
        else:
            return int(cod[0])+1

    def findMaxCodeUsers(self):
        self.connect()
        query = "SELECT MAX(user_ID) FROM users"
        self.cursor.execute(query)
        cod = self.cursor.fetchone()
        self.disconect()
        if cod[0] == None:
            return 200001
        else:
            return int(cod[0]) + 1

    def findMaxCodePlaces(self):
        self.connect()
        query = "SELECT MAX(site_ID) FROM sites"
        self.cursor.execute(query)
        cod = self.cursor.fetchone()
        self.disconect()
        if cod[0] == None:
            return 300001
        else:
            return int(cod[0]) + 1

    def findMaxCodeAnalizer(self):
        self.connect()
        query = "SELECT MAX(analizer_ID) FROM analizers"
        self.cursor.execute(query)
        cod = self.cursor.fetchone()
        self.disconect()
        if cod[0] == None:
            return 400001
        else:
            return int(cod[0]) + 1

    def getAllClients(self):
        self.connect()
        query ="SELECT * FROM clients WHERE client_ID != 100000"
        self.cursor.execute(query)
        clientsInfo = self.cursor.fetchall()
        self.disconect()
        return clientsInfo

    def getAllUsers(self, cod):
        self.connect()
        query ="SELECT * FROM users WHERE user_client = %s AND user_ID != 200000"
        self.cursor.execute(query, (cod,))
        usersInfo = self.cursor.fetchall()
        self.disconect()
        return usersInfo

    def getAllSites(self, cod):
        self.connect()
        query ="SELECT * FROM sites WHERE site_client = %s"
        self.cursor.execute(query, (cod,))
        sitesInfo = self.cursor.fetchall()
        self.disconect()
        return sitesInfo

    def getAllAnalizers(self):
        self.connect()
        query ="SELECT * FROM analizers"
        self.cursor.execute(query)
        analizersInfo = self.cursor.fetchall()
        self.disconect()
        return analizersInfo

    def searchClient(self, cod):
        self.connect()
        query ="SELECT * FROM clients WHERE client_ID = %s"
        self.cursor.execute(query, (cod,))
        clientInfo = self.cursor.fetchone()
        self.disconect()
        return clientInfo

    def searchUser(self, cod):
        self.connect()
        query ="SELECT * FROM users WHERE user_ID = %s"
        self.cursor.execute(query, (cod,))
        userInfo = self.cursor.fetchone()
        self.disconect()
        return userInfo

    def searchPlace(self, cod):
        self.connect()
        query ="SELECT * FROM sites WHERE site_ID = %s"
        self.cursor.execute(query, (cod,))
        placeInfo = self.cursor.fetchone()
        self.disconect()
        return placeInfo

    def searchAnalizer(self, cod):
        self.connect()
        query ="SELECT * FROM analizers WHERE analizer_ID = %s"
        self.cursor.execute(query, (cod,))
        analizerInfo = self.cursor.fetchone()
        self.disconect()
        return analizerInfo

    def addClient(self, Cod, Nom, Pay, Sus, Dir, Ciu, Est, Tel):
        self.connect()
        query = "INSERT INTO clients VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (Cod, Nom, Pay, Sus, Dir, Ciu, Est, Tel)
        self.cursor.execute(query, data)
        self.database.commit()
        self.disconect()

    def addUser(self, Cod, Nom, Pwd, Tip, Cor, Nic, Cli):
        self.connect()
        query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (Cod, Nom, Pwd, Tip, Cor, Cli, Nic)
        self.cursor.execute(query, data)
        self.database.commit()
        self.disconect()

    def addPlace(self, Cod, Nom, Ubi, Cli):
        self.connect()
        query = "INSERT INTO sites VALUES (%s, %s, %s, %s)"
        data = (Cod, Nom, Ubi, Cli)
        self.cursor.execute(query, data)
        self.database.commit()
        self.disconect()

    def addAnalizer(self, Cod, Fab, Use, Cla):
        self.connect()
        query = "INSERT INTO analizers VALUES (%s, %s, %s, %s)"
        data = (Cod, Fab, Use, Cla)
        self.cursor.execute(query, data)
        self.database.commit()
        self.disconect()

    def updateClient(self, Cod, Nom, Dir, Ciu, Est, Tel, Sus, Pay):
        self.connect()
        query ="UPDATE clients SET client_name = %s, client_address = %s, client_city = %s, client_state = %s, client_phone = %s, subscription_flag = %s, payment_flag = %s WHERE client_ID = %s"
        self.cursor.execute(query, (Nom, Dir, Ciu, Est, Tel, Sus, Pay, Cod))
        self.database.commit()
        self.disconect()

    def updateUser(self, Cod, Nom, Pas, Tip, Cor, Nic):
        self.connect()
        query ="UPDATE users SET user_name = %s, user_pass = %s, user_type = %s, email = %s, nick = %s WHERE user_ID = %s"
        self.cursor.execute(query, (Nom, Pas, Tip, Cor, Nic, Cod))
        self.database.commit()
        self.disconect()

    def updatePlace(self, Cod, Nom, Loc):
        self.connect()
        query ="UPDATE sites SET site_name = %s, site_location = %s WHERE site_ID = %s"
        self.cursor.execute(query, (Nom, Loc, Cod))
        self.database.commit()
        self.disconect()

    def updateAnalizer(self, Cod, Fab, Uso, Cla):
        self.connect()
        query ="UPDATE analizers SET manufacturer_name = %s, usage_flag = %s, class_name = %s WHERE analizer_ID = %s"
        self.cursor.execute(query, (Fab, Uso, Cla, Cod))
        self.database.commit()
        self.disconect()

    def delClient(self, cod):
        self.connect()
        query ="DELETE FROM clients WHERE client_ID = %s"
        self.cursor.execute(query, (cod,))
        self.database.commit()
        self.disconect()

    def delUser(self, cod):
        self.connect()
        query ="DELETE FROM users WHERE user_ID = %s"
        self.cursor.execute(query, (cod,))
        self.database.commit()
        self.disconect()

    def delPlace(self, cod):
        self.connect()
        query ="DELETE FROM sites WHERE site_ID = %s"
        self.cursor.execute(query, (cod,))
        self.database.commit()
        self.disconect()

    def delAnalizer(self, cod):
        self.connect()
        query ="DELETE FROM analizers WHERE analizer_ID = %s"
        self.cursor.execute(query, (cod,))
        self.database.commit()
        self.disconect()

    def searchLogin(self, username, password):
        self.connect()
        query ="SELECT user_name, user_type, email, nick, user_client FROM users WHERE nick = %s AND user_pass = %s"
        self.cursor.execute(query, (username, password))
        userInfo = self.cursor.fetchone()
        if userInfo != None:
            query = "SELECT client_name, client_ID FROM clients WHERE client_ID = %s"
            self.cursor.execute(query, (userInfo[4],))
            clientInfo = self.cursor.fetchone()
            userInfo += clientInfo
        self.disconect()
        return userInfo