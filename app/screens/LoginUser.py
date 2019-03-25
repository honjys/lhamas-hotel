import tkinter as tk
#from PIL import ImageTk, Image


class Login(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        '''self.imgGetter = Image.open("app/img/login.png")
        self.imgResizer = self.imgGetter.resize((300, 200), Image.ANTIALIAS)
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
        if self.nomeipt.get() == 'joao' and self.passwordipt.get() == '666':
            self.parent.session='admin'
            self.destroy()
            self.parent.show_adminscreen()
        else:
            self.parent.session='funcionario'
            self.destroy()
            self.parent.show_funcionarioscreen()
    