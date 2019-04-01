import tkinter as tk
from tkinter import messagebox



class FuncionarioScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.quartosB=tk.Button(self,    text=' Lista de Quartos',command=self.quartos)        
        self.clientesB = tk.Button(self, text='Lista de Clientes',command=self.clientes)        
        self.cadastroB = tk.Button(self, text='Cadastrar Cliente',command=self.cadastra)        
        self.horariosB = tk.Button(self, text='      Ver Horários  ', command=self.horario)
        self.logoff=tk.Button(self,      text='  Log off', command = self.sair)
        self.largura =35
        self.altura = 10
        self.quartosB.grid(row=0,column=0, ipadx=self.largura, ipady=self.altura)
        self.clientesB.grid(row=0,column=1, ipadx=self.largura, ipady=self.altura)
        self.cadastroB.grid(row=0,column=2,  ipadx=self.largura -10, ipady=self.altura)
        self.horariosB.grid(row=1,column=0,  ipadx=self.largura - 2, ipady=self.altura)
        self.logoff.grid(row=1,column = 2, ipadx=self.largura +20, ipady=self.altura)
        self.menu = tk.Menu(self)
        
    def quartos(self):
        messagebox.showerror('Error','Inacabado')

    def clientes(self):
        self.destroy()
        self.parent.show_Lista()
        
    def cadastra(self):
    	self.destroy()
    	self.parent.show_cadastrar()
    def horario(self):
    	messagebox.showerror("ERROR", "Em construção")

    def sair(self):
        self.parent.session=None
        self.destroy()
        self.parent.show_login()