import mysql.connector

conn = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="safe&SOUND96",
   database="epsol_bd"
)

cursor = conn.cursor()

def findMaxCodeClients():
    query = "SELECT MAX(client_ID) FROM clients"
    cursor.execute(query)
    cod = cursor.fetchone()
    
    if cod[0] == None:
        return 100001
    else:
        return int(cod[0])+1

def findMaxCodeUsers():
    query = "SELECT MAX(user_ID) FROM users"
    cursor.execute(query)
    cod = cursor.fetchone()

    if cod[0] == None:
        return 200001
    else:
        return int(cod[0]) + 1

def findMaxCodePlaces():
    query = "SELECT MAX(site_ID) FROM sites"
    cursor.execute(query)
    cod = cursor.fetchone()

    if cod[0] == None:
        return 300001
    else:
        return int(cod[0]) + 1

def findMaxCodeAnalizer():
    query = "SELECT MAX(analizer_ID) FROM analizers"
    cursor.execute(query)
    cod = cursor.fetchone()

    if cod[0] == None:
        return 400001
    else:
        return int(cod[0]) + 1

def getAllClients():
    query ="SELECT * FROM clients"
    cursor.execute(query)
    clientsInfo = cursor.fetchall()
    return clientsInfo

def getAllUsers():
    query ="SELECT * FROM users"
    cursor.execute(query)
    usersInfo = cursor.fetchall()
    return usersInfo

def getAllSites():
    query ="SELECT * FROM sites"
    cursor.execute(query)
    sitesInfo = cursor.fetchall()
    return sitesInfo

def getAllAnalizers():
    query ="SELECT * FROM analizers"
    cursor.execute(query)
    analizersInfo = cursor.fetchall()
    return analizersInfo

def searchClient(cod):
    query ="SELECT * FROM clients WHERE client_ID = %s"
    cursor.execute(query, (cod,))
    clientInfo = cursor.fetchone()
    return clientInfo

def searchUser(cod):
    query ="SELECT * FROM users WHERE user_ID = %s"
    cursor.execute(query, (cod,))
    userInfo = cursor.fetchone()
    return userInfo

def searchPlace(cod):
    query ="SELECT * FROM sites WHERE site_ID = %s"
    cursor.execute(query, (cod,))
    placeInfo = cursor.fetchone()
    return placeInfo

def searchAnalizer(cod):
    query ="SELECT * FROM analizers WHERE analizer_ID = %s"
    cursor.execute(query, (cod,))
    analizerInfo = cursor.fetchone()
    return analizerInfo

def addClient(Cod, Nom, Pay, Sus, Dir, Ciu, Est, Tel):
    query = "INSERT INTO clients VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    data = (Cod, Nom, Pay, Sus, Dir, Ciu, Est, Tel)
    cursor.execute(query, data)
    conn.commit()

def addUser(Cod, Nom, Pwd, Tip, Cor, Nic, Cli):
    query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (Cod, Nom, Pwd, Tip, Cor, Cli, Nic)
    cursor.execute(query, data)
    conn.commit()

def addPlace(Cod, Nom, Ubi, Cli):
    query = "INSERT INTO sites VALUES (%s, %s, %s, %s)"
    data = (Cod, Nom, Ubi, Cli)
    cursor.execute(query, data)
    conn.commit()

def addAnalizer(Cod, Fab, Use, Cla):
    query = "INSERT INTO analizers VALUES (%s, %s, %s, %s)"
    data = (Cod, Fab, Use, Cla)
    cursor.execute(query, data)
    conn.commit()

def updateClient(Cod, Nom, Dir, Ciu, Est, Tel):
    query ="UPDATE clients SET client_name = %s, client_address = %s, client_city = %s, client_state = %s, client_phone = %s WHERE client_ID = %s"
    cursor.execute(query, (Nom, Dir, Ciu, Est, Tel, Cod))
    conn.commit()

def updateUser(Cod, Nom, Pas, Tip, Cor, Nic):
    query ="UPDATE users SET user_name = %s, user_pass = %s, user_type = %s, email = %s, nick = %s WHERE user_ID = %s"
    cursor.execute(query, (Nom, Pas, Tip, Cor, Nic, Cod))
    conn.commit()

def updatePlace(Cod, Nom, Loc):
    query ="UPDATE sites SET site_name = %s, site_location = %s WHERE site_ID = %s"
    cursor.execute(query, (Nom, Loc, Cod))
    conn.commit()

def updateAnalizer(Cod, Fab, Uso, Cla):
    query ="UPDATE analizers SET manufacturer_name = %s, usage_flag = %s, class_name = %s WHERE analizer_ID = %s"
    cursor.execute(query, (Fab, Uso, Cla, Cod))
    conn.commit()

def delClient(cod):
    query ="DELETE FROM clients WHERE client_ID = %s"
    cursor.execute(query, (cod,))
    conn.commit()

def delUser(cod):
    query ="DELETE FROM users WHERE user_ID = %s"
    cursor.execute(query, (cod,))
    conn.commit()

def delPlace(cod):
    query ="DELETE FROM sites WHERE site_ID = %s"
    cursor.execute(query, (cod,))
    conn.commit()

def delAnalizer(cod):
    query ="DELETE FROM analizers WHERE analizer_ID = %s"
    cursor.execute(query, (cod,))
    conn.commit()

def searchLogin(username, password):
    query ="SELECT user_ID, user_name FROM users WHERE user_name = %s AND user_pass = %s"
    cursor.execute(query, (username, password))
    userInfo = cursor.fetchone()
    return userInfo