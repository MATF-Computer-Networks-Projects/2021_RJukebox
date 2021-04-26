import mysql.connector
from db_templates.load_template import load_db_template

def create_table(cursor, template_name: str,primary_key: str,foreign_key: str = ""):
  
  template = load_db_template(template_name)

  query=template.render(primary_key=primary_key,foreign_key=foreign_key)

  cursor.execute(query)
