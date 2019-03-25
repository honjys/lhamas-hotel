from tkinter import messagebox
import tkinter as tk
from app.database.ClientesRepo import ClienteRepo
from app.models.Cliente import Cliente


class Cadastrar(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.clicrepo = ClienteRepo()
        self.nometxt = tk.Label(self,text='Nome completo:')
        self.cpftxt = tk.Label(self,text='Informe seu CPF(apenas numeros):')
        self.emailtxt=tk.Label(self, text='Email:')
        self.numerotxt = tk.Label(self, text='Telefone:')
        
        self.nomeipt = tk.Entry(self)
        self.cpfipt=tk.Entry(self)
        self.emailipt = tk.Entry(self)
        self.numeroipt=tk.Entry(self)
                
        self.enter=tk.Button(self,text='Confirmar', command=self.confirm)
        self.cancelarB = tk.Button(self,text='Voltar', command = self.backf)

        self.nometxt.grid(row=0,column=0)
        self.nomeipt.grid(row=0,column=1)
        self.cpftxt.grid(row=2,column=0)
        self.cpftxt.grid(row=2,column=0)
        self.cpfipt.grid(row=2,column=1)
        self.emailtxt.grid(row=3,column=0)
        self.emailipt.grid(row=3,column=1)
        self.numerotxt.grid(row=4,column=0)
        self.numeroipt.grid(row=4,column=1)
        self.cancelarB.grid(row=5,column=0)
        self.enter.grid(row=5,column=1)      
    
    def confirm(self):
        func = Cliente(self.cpfipt.get(), self.nomeipt.get(), self.emailipt.get(), self.numeroipt.get())
        self.clicrepo.add_cliente(func)
        self.destroy()
        self.parent.clear_campo()

    def backf(self):
        self.destroy()
        self.parent.show_funcionarioscreen()