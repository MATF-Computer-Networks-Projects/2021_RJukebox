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
query="""CREATE TABLE users (
            id INT UNSIGNED AUTO_INCREMENT NOT NULL,
            user VARCHAR(255), 
            password VARCHAR(255),
            PRIMARY KEY (id))"""
mycursor.execute(query)

mycursor.close()
mydb.close()

