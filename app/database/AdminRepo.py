from app.database.database import DatabaseConnection
from tkinter import messagebox



class AdminDB:
    def __init__(self):

        self.connection = DatabaseConnection.get_connection()

    def check_admin(self, cpfipt, senhaipt):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cpf,senha FROM admin")
            results = cursor.fetchall()
            for result in results:
                if cpfipt==result[0] and senhaipt==result[1]:
                    return True
        except Exception:
            return messagebox.showerror("ERROR", "Algo não funvionou :/")