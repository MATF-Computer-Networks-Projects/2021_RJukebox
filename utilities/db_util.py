from dotenv import dotenv_values
import mysql.connector

def connect_to_db(db: str=""):
  config = dotenv_values(".env")
  try:
    if len(db)==0:
      mydb = mysql.connector.connect(
        host="localhost",
        user=config['USER'],
        password=config['PASSWORD'],
      )
    else:
      mydb = mysql.connector.connect(
        host="localhost",
        user=config['USER'],
        password=config['PASSWORD'],
        database=db,
      )
    return mydb
  except Exception as e:
    print(f"Exception happend while connecting to db:{e}")
    return None

def execute_query(query : str,cursor):
  try:
    result = cursor.execute(query)
    return result
  except Exception as e:
    print(f"Failure while executing query [{query}]:{e}")
    return None

def check_if_exists(cursor, db : str, query) -> bool:
  cursor.execute(query)
  result=[]
  for x in cursor:
    result.append(str(x)[2:-3])
  if db in result:
    return True
  else:
    return False