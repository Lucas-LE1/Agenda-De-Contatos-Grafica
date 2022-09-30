
# contacts_archive = open("contacts.txt","a+")
# contacts_archive.close()

from asyncio.windows_events import NULL
import json
import os.path
from tkinter import END
from zipapp import create_archive


class Contacts():

    def __init__(self):

        self.create_archive()

    def create_archive(self):
        if (os.path.isfile('contacts.json')):
            self.contacts_archive = open('contacts.json', 'r')
            if self.contacts_archive.read() == '':
                self.contacts_archive.close()
                self.write_archive()

            print("Arquivo Existente")
        else:
            self.write_archive()
            print("Criando arquivo de contatos")

    def write_archive(self):
        self.contacts_archive = open('contacts.json', 'w')
        self.contacts_archive.write('[]')
        self.contacts_archive.close()

    def new_contato(self):

        self.contacts_archive = open('contacts.json', 'r')

        dictionary = {
            "codigo": 1,
            "NOME": self.in_nome.get(),
            "CPF": self.in_cpf.get(),
            "E-MAIL": self.in_email.get()
        }

        contacts = []

        contacts = json.load(self.contacts_archive)

        self.contacts_archive.close()

        contacts.append(dictionary)

        self.contacts_archive = open('contacts.json', 'w')

        json_object = json.dumps(contacts, indent=2, separators=[
                                 ",", ':'], sort_keys=True)
        self.contacts_archive.writelines(json_object)

        for i in self.contatos_list.get_children():
            self.contatos_list.delete(i)

        for contact in contacts:

            self.contatos_list.insert('', END,
                                      values=(
                                          contact['codigo'],
                                          contact['NOME'],
                                          contact['CPF'],
                                          contact['E-MAIL']
                                      ))

        else:
            del contacts
            del dictionary

        self.contacts_archive.close()
