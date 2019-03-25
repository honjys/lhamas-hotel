import psycopg2

class DatabaseConnection():

    @staticmethod
    def get_connection():
        conn = psycopg2.connect('dbname=ifpb user=postgres host=localhost port=5432')
        conn.autocommit = True
        return conn
