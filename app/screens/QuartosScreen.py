import tkinter as tk
from app.database.QuartosRepo import Quarto
from app.models.Quartos import Quarto

class Quartos(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT numero,metros2, aluguel_dia,status FROM quartos")
            
        except Exception:
            return messagebox.showerror("ERROR", "Algo deu errado :/")
            
    def voltarf(self):
        if self.parent.session == 'admin':
            self.destroy()
            self.parent.show_adminscreen()
            
        elif self.parent.session == 'funcionario':
            self.destroy()
            self.parent.show_funcionarioscreen()