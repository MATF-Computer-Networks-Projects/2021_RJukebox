import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv("USER"),
  password=os.getenv("PASSWORD"),
  database="RJukebox"
)

mycursor = mydb.cursor()
query="""CREATE TABLE users (
            user VARCHAR(255), 
            password VARCHAR(255), 
            token VARCHAR(255) NOT NULL, 
            PRIMARY KEY (token))"""
mycursor.execute(query)

mycursor.close()
mydb.close()

