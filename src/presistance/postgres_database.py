from .database_interface import DatabaseInterface
import psycopg2
import configparser
import os
import urllib.parse as urlparse
import re
from flask import current_app


database_config = configparser.ConfigParser() 
dir_path = os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(dir_path, '../../configuration/database_config.ini')
database_config.read(filename)

queries_config = configparser.ConfigParser() 
dir_path = os.path.dirname(os.path.realpath(__file__))
filename=os.path.join(dir_path, '../../configuration/postgres_queries.ini')
queries_config.read(filename)


class PostgresDatabase(DatabaseInterface):
    def __init__(self):
        self.connection = None
        pass

    def get_connection(self):
        return psycopg2.connect(
            user = "postgres",
            password = "Ravi@143",
            host = "localhost",
            port = 5432,
            database = "mydatabase")

    def fetch_all(self, table_name):
        self.connection = self.get_connection()

        ################################################################

        cursor = self.connection.cursor()
        fetch_all_query = queries_config[table_name]["fetch_all_query"]
        #print("fetch_all_query: {}".format(fetch_all_query))
        try:
            cursor.execute(fetch_all_query)
            db_result = cursor.fetchall()
            #print("type db_result: {}".format(type(db_result)))
            # it = iter(db_result)
            # db_result_dict = dict(zip(it, it))
            # return db_result_dict
            return db_result
            # print(type(algorithmResult))
        except psycopg2.Error as error:
            #self.connection.rollback()
            print("Error while fetch_all: ", error)
            return 
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                # print("PostgreSQL connection is closed")