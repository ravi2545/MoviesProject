from .postgres_database import PostgresDatabase

class DatabaseFactory:
    def __init__(self):
        pass

    def get_database_connection(self, database_name):
        if database_name.lower()=='POSTGRES'.lower():
            return PostgresDatabase()
                