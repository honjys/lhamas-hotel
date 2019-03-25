import tkinter as tk

class FirstScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.Bcadastro = tk.Button(self, text='Cadastrar', command=self.cadastro)
        self.Bcadastro.grid(row=0,column=1)
        self.Bquartos = tk.Button(self, text ='Quartos',  command = self.quartos)
        self.Bquartos.grid(row=0,column=2)
    
    def quartos(self):
        self.destroy()

    def cadastro(self):
        self.destroy()
        self.parent.show_cadastrar()