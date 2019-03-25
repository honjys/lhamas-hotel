import tkinter as tk 
from tkinter import messagebox
from app.database.FuncionarioRepo import FuncionarioRepo
from app.models.Funcionario import Funcionario



class CadastraFuncio(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.funcrepo = FuncionarioRepo()
        self.nometxt=tk.Label(self, text='Nome:')
        self.cpftxt = tk.Label(self,text='CPF:')
        self.emailtxt = tk.Label(self,text='Email:')
        self.numerotxt = tk.Label(self, text = 'Numero de Contato:')
        self.passwordtxt = tk.Label(self, text='Digite uma senha:')
        
        self.nomeipt=tk.Entry(self)
        self.cpfipt= tk.Entry(self)
        self.emailipt= tk.Entry(self)
        self.numeroipt= tk.Entry(self)
        self.passwordipt= tk.Entry(self,show = '*')
        
        self.cancelarB = tk.Button(self, text='Voltar', command = self.cancelar)
        self.confirmarB=tk.Button(self, text = 'Confirmar', command = self.confirmar)

        self.nometxt.grid(row=0 ,column =0 )
        self.cpftxt.grid(row=1 ,column = 0)
        self.emailtxt.grid(row=2 ,column =0 )
        self.numerotxt.grid(row=3 ,column =0 )
        self.passwordtxt.grid(row=4 ,column =0 )
        
        self.nomeipt.grid(row=0 ,column =1 )
        self.cpfipt.grid(row=1 ,column =1 )
        self.emailipt.grid(row=2 ,column = 1)
        self.numeroipt.grid(row=3 ,column = 1)
        self.passwordipt.grid(row=4 ,column =1 )
        self.cancelarB.grid(row= 5, column= 0)
        self.confirmarB.grid(row=5, column = 1)
        
    def confirmar(self):
        func = Funcionario(self.cpfipt.get(), self.nomeipt.get(), self.emailipt.get(), self.numeroipt.get(), self.passwordipt.get())
        self.funcrepo.add_funcionario(func)
        self.destroy()
        self.parent.clear_campoF()

    def cancelar(self):
        self.destroy()
        self.parent.show_adminscreen()
        