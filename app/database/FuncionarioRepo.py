from app.database.database import DatabaseConnection
from app.models.Funcionario import Funcionario
from tkinter import messagebox

class FuncionarioRepo:
    def __init__(self):
        self.connection = DatabaseConnection.get_connection()

    def add_funcionario(self, funcionario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO funcionario (cpf, nome, email, telefone, senha) VALUES ('%s', '%s', '%s', '%s', '%s')" %(funcionario.cpf, funcionario.nome, funcionario.email, funcionario.telefone, funcionario.senha))
            return True
        except Exception:
            return messagebox.showerror("ERROR", "Algo não funvionou :/")

    def check_funcionario(self, cpfipt, senhaipt):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT cpf,senha FROM funcionario")
            results = cursor.fetchall()
            for result in results:
                if cpfipt==result[0] and senhaipt==result[1]:
                    return True
        except Exception:
            return messagebox.showerror("ERROR", "Algo não funvionou :/")

    def look_Funcionario(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT cpf, nome, email, telefone, senha FROM funcionario')
            cursor.fetchall()
            print(cursor)
        except Exception:
            messagebox.showerror('Error','Não foi')