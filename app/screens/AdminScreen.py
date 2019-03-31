import tkinter as tk
from tkinter import messagebox
import sys


class AdminScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.quartosB=tk.Button(self, text=' Lista de Quartos',command=self.quartos)                
        self.horariosB = tk.Button(self, text ='Ver Horários', command=self.horario)
        self.funcionariosB = tk.Button(self, text ='Lista de Funcionarios', command=self.cadasfuncio)
        self.clientesB = tk.Button(self,text='Lista de Clientes',command=self.clientes)
        self.logoff=tk.Button(self, text = 'Log off', command = self.sair)

        self.quartosB.pack()
        self.horariosB.pack()
        self.funcionariosB.pack()
        self.clientesB.pack()
        self.logoff.pack()

    def quartos(self):
        messagebox.showerror('ERROR',"você não fez ainda")

    def clientes(self):
        messagebox.showerror('ERROR',"você não fez ainda")

    def horario(self):
        messagebox.showerror("ERROR", "você não fez ainda")

    def cadasfuncio(self):
        self.destroy()
        self.parent.show_cadastrafuncionario()
        
    def sair(self):
        self.parent.session=None
        self.destroy()
        self.parent.show_login()