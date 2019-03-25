import tkinter as tk


class Clientes(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.passa=tk.Label(self,text='Em construção')
        self.voltar = tk.Button(self, text = 'Voltar',command=self.voltarf)

        self.passa.grid(row=0,column=1)
        self.voltar.grid(row=0,column=0)

    def voltarf(self):
        if self.parent.session == 'admin':
            self.destroy()
            self.parent.show_adminscreen()
            
        elif self.parent.session == 'funcionario':
            self.destroy()
            self.parent.show_funcionarioscreen()