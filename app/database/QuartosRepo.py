from app.database.database import DatabaseConnection
from app.models.Quartos import Quarto
from tkinter import messagebox

class QuartoRepo():
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

        def add_reserva(self, Quarto):
            try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO funcionario (cpf, nome, email, telefone, senha) VALUES ('%s', '%s', '%s', '%s', '%s')" %(funcionario.cpf, funcionario.nome, funcionario.email, funcionario.telefone, funcionario.senha))
            return True
        except Exception:
            return messagebox.showerror("ERROR", "Algo deu errado :/")