import jwt
import json
import mysql.connector
import os
from dotenv import dotenv_values
from create_users import create_users

def input_user(mydb, cursor):
  create_users()

  with open("users.json") as json_file:
      data = json.load(json_file)

  for d in data['users']:
      cursor.execute("INSERT INTO users (user,password) VALUES (%s,%s)",(d['user'], d['password']))

  mydb.commit()
  print("Users added.")