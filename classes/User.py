import logging

from utilities.hash_utilities import generate_hash
from utilities.db_util import connect_execute_query


class User:
    def __init__(self,name,password):
        self.name=name;
        self.password=password
    
    
    def validate_user(self) -> bool:
        query=f"SELECT user FROM users WHERE user=\'{self.name}\'"
        result=connect_execute_query(query)
        if result:
            logging.warning(f"User by the name {result[0][0]} already exists.")
            return False
        else:
            logging.info(f"User with name {self.name} is valid.")
            return True


    def input_user(self) -> bool:
        if self.validate_user():
            logging.info("Adding user into db.")
            query=f"INSERT INTO users (user, password) VALUES {self.name, generate_hash(self.password)}"
            result=connect_execute_query(query)
            return True
        else:
            return False
