import tkinter as tk
from app.database.AdminRepo import AdminDB
from app.database.FuncionarioRepo import FuncionarioRepo
from app.database.database import DatabaseConnection
#from PIL import ImageTk, Image


class Login(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        '''self.imgGetter = Image.open("app/img/login.png")
        self.imgResizer = self.imgGetter.resize((200, 100), Image.ANTIALIAS)
        self.userImg = ImageTk.PhotoImage(self.imgResizer)
        self.img = tk.Label(image=self.userImg, highlightthickness=0, bd=0)
        self.img.pack()'''
        self.nometxt=tk.Label(self,text='CPF do funcionário:')        
        self.nomeipt = tk.Entry(self)        
        self.passwordtxt=tk.Label(self,text='Senha:')        
        self.passwordipt=tk.Entry(self, show="*")               
        self.confirmar=tk.Button(self, text='Confirmar', command=self.logar)
        self.sair = tk.Button(self,text='Sair', command = quit)

        self.nometxt.pack()
        self.nomeipt.pack()
        self.passwordtxt.pack()
        self.passwordipt.pack()
        self.confirmar.pack(side=tk.LEFT)
        self.sair.pack(side=tk.RIGHT)
        
    def logar(self):
        #get
        self.cpf = self.nomeipt.get()
        self.senha = self.passwordipt.get()
        self.dbf = FuncionarioRepo()
        self.db = AdminDB()

        if (self.db.check_admin(self.cpf, self.senha)):
            self.parent.session='admin'
            self.destroy()
            self.parent.show_adminscreen()
        elif (self.dbf.check_funcionario(self.cpf, self.senha)):
            self.parent.session='funcionario'
            self.destroy()
            self.parent.show_funcionarioscreen()
    