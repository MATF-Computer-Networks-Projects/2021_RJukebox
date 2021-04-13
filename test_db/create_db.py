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
  password=os.getenv("PASSWORD")
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE RJukebox")

mycursor.close()
mydb.close()

