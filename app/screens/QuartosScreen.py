import tkinter as tk


class Quartos(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def voltarf(self):
        if self.parent.session == 'admin':
            self.destroy()
            self.parent.show_adminscreen()
            
        elif self.parent.session == 'funcionario':
            self.destroy()
            self.parent.show_funcionarioscreen()