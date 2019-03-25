import tkinter as tk
from app.database.QuartosRepo import Quarto
from app.models.Quartos import Quarto

class Quartos(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def voltarf(self):
            self.destroy()
            self.parent.show_funcionarioscreen()