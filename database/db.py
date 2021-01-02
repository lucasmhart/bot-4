from mysql.connector import (connection)

class DB:
    db_host = 'localhost'
    db_user = 'project'
    db_password = 'project'
    db_name = 'bot'
    db_connection = None

    def connect():
        self.db_connection = connection.MySQLConnection(
            host=self.db_host, 
            user=self.db_user, 
            password=self.db_password, 
            database=self.db_name)
    
    def close():
        self.db_connection.close()
    
    def insert(script):
        self.connect()
        