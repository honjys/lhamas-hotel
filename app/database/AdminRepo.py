from app.database.database import DatabaseConnection
from app.models.Admin import Admin
from tkinter import messagebox

class AdminRepo:
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

    def check_admin(self, cpfipt, senhaipt):
        self.cpfipt = cpfipt
        self.senhaipt = senhaipt
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cpf,senha FROM admin")
            

            return True
        except Exception:
            return messagebox.showerror("ERROR", "Algo não funvionou :/")