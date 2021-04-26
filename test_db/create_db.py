import mysql.connector
from test_db.create_table import create_table
from test_db.users_input import input_user
from utilities.db_util import connect_to_db, execute_query,check_if_exists

mydb=connect_to_db()
if not mydb:
  raise Exception(f"Connecting to db unsuccessful.")

mycursor=mydb.cursor()
if not check_if_exists(mycursor,"RJukebox","SHOW DATABASES"):
  query="CREATE DATABASE RJukebox"
  execute_query(query,mycursor)

mycursor.close()
mydb.close()

mydb=connect_to_db("RJukebox")
mycursor=mydb.cursor()

if not check_if_exists(mycursor,"users","SHOW TABLES"):
  create_table( mycursor, 'user_table.template', 'id')
if not check_if_exists(mycursor,"songs","SHOW TABLES"):
  create_table( mycursor, 'song_table.template', 'id')
if check_if_exists(mycursor,"users","SHOW TABLES"):
  input_user(mydb,mycursor)

mycursor.close()
mydb.close()