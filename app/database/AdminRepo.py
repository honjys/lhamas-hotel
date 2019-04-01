from app.database.database import DatabaseConnection
from tkinter import messagebox


class AdminDB:
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

    def check_admin(self, cpfipt, senhaipt):
        self.cpfipt = cpfipt
        self.senhaipt = senhaipt
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cpf,senha FROM admin")
            print(cursor.fetch)
            for cpf,senha in cursor.fetch:
                if cpf == cpfipt:
                    if senha == senhaipt:
                        return True
        except Exception:
            return cursor.fetch