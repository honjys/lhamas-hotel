from app.database.database import DatabaseConnection
from app.models.Quartos import Quarto
from tkinter import messagebox


class QuartoRepo():
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

    def verQ(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT numero,metros2, aluguel_dia,status FROM quartos")
            return True
            
        except Exception:
            return messagebox.showerror("ERROR", "Algo deu errado :/"), messagebox.showerror('Error','inacabado')