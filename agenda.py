from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
from tokenize import String

janela = Tk()
texto1 = String
lista = []

class Funcs():
    def new_contato(self):
        # lista.append((self.in_pesquisar.get(),self.in_pesquisar.get(),self.in_pesquisar.get(),self.in_pesquisar.get()))
        self.contatos_list.insert("",'end',values=(self.in_pesquisar.get(),self.in_pesquisar.get(),self.in_pesquisar.get(),self.in_pesquisar.get()))

class Application(Funcs):
    def __init__(self):
        self.janela = janela
        self.Tela()
        self.frames_de_tela()
        self.criar_botoes()
        self.input_pesquisar()
        self.lista_contatos()
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
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.45)
    def criar_botoes(self):
        self.bt_novo = Button(self.frame_1,text="Novo", command=self.new_contato)
        self.bt_novo.place(relx=0.2, rely= 0.02, relwidth= 0.10, relheight= 0.15)

        self.bt_limpar = Button(self.frame_1,text="Limpar", command=NULL)
        self.bt_limpar.place(relx=0.3, rely= 0.02, relwidth= 0.10, relheight= 0.15)

        self.bt_excluir = Button(self.frame_1,text="Excluir", command=NULL)
        self.bt_excluir.place(relx=0.7, rely= 0.02, relwidth= 0.10, relheight= 0.15)

        self.bt_atualizar = Button(self.frame_1,text="Atualizar", command=NULL)
        self.bt_atualizar.place(relx=0.8, rely= 0.02, relwidth= 0.10, relheight= 0.15)
    def input_pesquisar(self):
        self.label_pesquisar = Label(self.frame_1, text="Código")
        self.label_pesquisar.place(relx=0.06,rely=0.05, relwidth=0.05)
        self.in_pesquisar = Entry(self.frame_1)
        self.in_pesquisar.place(relx=0.055, rely= 0.15, relwidth=0.06)

        self.label_pesquisar = Label(self.frame_1, text="Nome:")
        self.label_pesquisar.place(relx=0.06,rely=0.40, relwidth=0.05,height=30)
        self.in_pesquisar = Entry(self.frame_1)
        self.in_pesquisar.place(relx=0.12, rely= 0.40, relwidth=0.8,height=30)

        self.label_pesquisar = Label(self.frame_1, text="CPF:")
        self.label_pesquisar.place(relx=0.06,rely=0.565, relwidth=0.05,height=30)
        self.in_pesquisar = Entry(self.frame_1)

        self.in_pesquisar.place(relx=0.12, rely= 0.565, relwidth=0.325,height=30)

        self.label_pesquisar = Label(self.frame_1, text="Email:")
        self.label_pesquisar.place(relx=0.46,rely=0.565, relwidth=0.05,height=30)
        self.in_pesquisar = Entry(self.frame_1)
        self.in_pesquisar.place(relx=0.52, rely= 0.565, relwidth=0.4,height=30)
    def teste(self):
        print(self.in_pesquisar.get()) 
    def lista_contatos(self):
        self.contatos_list = ttk.Treeview(self.frame_2, columns=['col1','col2','col3','col4'], height=3)

        self.contatos_list.heading('#0')
        self.contatos_list.heading('#1',text='CÓDIGO')
        self.contatos_list.heading('#2',text='NOME')
        self.contatos_list.heading('#3',text='CPF')
        self.contatos_list.heading('#4',text='E-MAIL')


        self.contatos_list.column('#0',width=1)
        self.contatos_list.column('#1',width=20)
        self.contatos_list.column('#2',width=250)
        self.contatos_list.column('#3',width=100)
        self.contatos_list.column('#4',width=125)

        self.contatos_list.place(relx=0.02,rely=.05,relwidth=.95, relheight=.9)

        self.scroll_bar = Scrollbar(self.frame_2,orient='vertical')
        self.scroll_bar.place(relx=0.96,rely=0.1,relwidth=0.02, relheight=0.85)

        self.contatos_list.configure(yscroll = self.scroll_bar, yscrollcommand= self.scroll_bar.set)

        contacts = []
        for n in range(1, 100):
            contacts.append((f'codigo {n}',f'Okkkk {n}'))

        # add data to the treeview
        i=0
        self.contatos_list.insert("",'end',iid=i,
		values=(i,'Alex','Four',78,'Male'))
            


Application()