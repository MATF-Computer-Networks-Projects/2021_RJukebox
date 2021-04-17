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
query="""CREATE TABLE songs (
          id INT UNSIGNED AUTO_INCREMENT NOT NULL,
          song_name VARCHAR(255), 
          artist VARCHAR(255), 
          genre VARCHAR(255), 
          yt_link VARCHAR(255), 
          PRIMARY KEY (id))"""
mycursor.execute(query)

mycursor.close()
mydb.close()

