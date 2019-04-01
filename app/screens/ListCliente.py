import tkinter as tk
from app.database.AdminRepo import AdminDB
from app.database.FuncionarioRepo import FuncionarioRepo
from app.database.database import DatabaseConnection


class Listar(tk.Frame):
    def __init__(self, parent, results):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        lista = []
        for result in results:
            lista.append(tk.Label(self, text="%s %s %s %s" % (result[0], result[1], result[2], result[3],)))
        cont = 0 
        for cliente in lista:
            cliente.grid(row=cont, column=0)
            cont += 1