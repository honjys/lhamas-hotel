from app.database.database import DatabaseConnection
from app.models.Quartos import Quarto
from tkinter import messagebox

class QuartoRepo():
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

        def add_reserva(self, Quarto):
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO funcionario (numero,metros2, aluguel_dia,status) VALUES ('%s', '%s', '%s', '%s')" %(Quarto.numero, Quarto.metros2, Quarto.aluguel_dia, Quarto.status))
                return True
            except Exception:
                return messagebox.showerror("ERROR", "Algo deu errado :/")