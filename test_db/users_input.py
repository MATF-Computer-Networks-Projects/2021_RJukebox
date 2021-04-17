import jwt
import json
import mysql.connector
import os
from dotenv import dotenv_values

config = dotenv_values(".env")

with open("users.json") as json_file:
    data = json.load(json_file)

mydb = mysql.connector.connect(
  host="localhost",
  user=config['USER'],
  password=config['PASSWORD'],
  database="RJukebox"
)
mycursor = mydb.cursor()
for d in data['users']:
    print(d)
    mycursor.execute("INSERT INTO users (user,password) VALUES (%s,%s)",(d['user'], d['password']))

mydb.commit()
mycursor.close()
mydb.close()