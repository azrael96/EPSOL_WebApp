#Import the necessary libraries
from sqlalchemy.orm import declarative_base

#define the variables to make the conecction
driver = "mysqlconnector"
username = "root"
password = "safe&SOUND96"
server_port = "localhost"
database = "epsol_bd"

#Url string of the connection
connection_string ="mysql+"+driver+"://"+username+":"+password+"@"+server_port+"/"+database

#base model of the ORM database classes
Base = declarative_base()