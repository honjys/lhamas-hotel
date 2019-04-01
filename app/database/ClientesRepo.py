from app.database.database import DatabaseConnection
from app.models.Cliente import Cliente
from tkinter import messagebox

class ClienteRepo:
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

    def add_cliente(self, cliente):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO cliente (cpf, nome, email, telefone) VALUES ('%s', '%s', '%s', '%s')" %(cliente.cpf, cliente.nome, cliente.email, cliente.telefone))
            return True
        except Exception:
            return messagebox.showerror("ERROR", "Algo não funvionou :/")

    def show_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        results = cursor.fetchall() 
        return results
