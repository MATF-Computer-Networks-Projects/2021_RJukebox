import mysql.connector
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

mydb = mysql.connector.connect(
  host="localhost",
  user=config['USER'],
  password=config['PASSWORD'],
  database="RJukebox"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE RJukebox")

mycursor.close()
mydb.close()

