import tkinter as tk
from app.screens.FirstScreen import FirstScreen
from app.screens.LoginUser import Login
from app.screens.CadastroScreen import Cadastrar
from app.screens.FuncionarioScreen import FuncionarioScreen
from app.screens.ClientesScreen import Clientes
from app.screens.QuartosScreen import Quartos
from app.screens.AdminScreen import AdminScreen
from app.screens.CadastraFuncio import CadastraFuncio
from app.database.FuncionarioRepo import FuncionarioRepo


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Lhamas Hotel')
        self.geometry('700x400')
        self.session= None
        self.show_login()

    def show_funcionarioscreen(self):
    	self.funciotela = FuncionarioScreen(self)
    	self.funciotela.grid()

    def show_adminscreen(self):
        self.adm = AdminScreen(self)
        self.adm.grid()

    def show_login(self):
        self.login = Login(self)
        self.login.pack()

    def show_firstscreen(self):
        self.firstscreen = FirstScreen(self)
        self.firstscreen.grid()

    def show_cadastrar(self):
        self.cadastrar = Cadastrar(self)
        self.cadastrar.grid()

    def show_cadastrafuncionario(self):
        self.cadastrafuncio = CadastraFuncio(self)
        self.cadastrafuncio.grid()
    
    def show_clientes(self):
        self.clientes = Clientes(self)
        self.clientes.grid()
    
    def show_quartos(self):
        self.quartos=Quartos(self)
        self.quartos.grid()
        
    def clear_campo(self):
        self.cadastrar =Cadastrar(self)
        self.cadastrar.grid()
        
    def clear_campoF(self):
        self.cadastrafuncio = CadastraFuncio(self)
        self.cadastrafuncio.grid()

    def add_funcio(self):
        self.add_funcio = FuncionarioRepo()

root = App()
root.mainloop()