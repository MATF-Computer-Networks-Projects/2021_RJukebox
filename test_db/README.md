
- *MYSQL https://dev.mysql.com/downloads/installer/*


## .ENV Example

- *.env file has to be in root folder of the app*
- *USER="user" PASSWORD="password"*

## Running the scripts

- *Run the `create_db.py` to create the whole db.*

## create_db.py
- *setup_db(): creates the whole data base.*

## create_table.py
- *create_table(cursor, table_name, template_name: str, primary_key: str, foreign_key: str = ""): Create a table with table_name in db.*

## user_input.py
- *input_user(mydb, cursor)-> bool: inputs user into db.*
- *input_songs(mydb_, cursor) -> bool: inputs song into db.*