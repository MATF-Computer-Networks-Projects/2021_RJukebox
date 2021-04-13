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
query="""CREATE TABLE songs (
          song_name VARCHAR(255), 
          artist VARCHAR(255), 
          genre VARCHAR(255), 
          yt_link VARCHAR(255), 
          token VARCHAR(255), 
          FOREIGN KEY (token) REFERENCES users(token))"""
mycursor.execute(query)

mycursor.close()
mydb.close()

