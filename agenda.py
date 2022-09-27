from tkinter import *

janela = Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.Tela()
        self.frames_de_tela()
        janela.mainloop()
    def Tela(self):
        self.janela.title("Agenda De Contatos")
        self.janela.configure(background="#1e3743")
        self.janela.geometry("788x588")
        self.janela.resizable(TRUE,TRUE)
        self.janela.maxsize(988,788)
        self.janela.minsize(588,388)
    def frames_de_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg="#c2c2d6")
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.45)
        self.frame_2 = Frame(self.janela, bd=4, bg="#c2c2d6")
        self.frame_2.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.45)


Application()