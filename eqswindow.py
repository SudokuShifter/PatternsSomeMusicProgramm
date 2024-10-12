from tkinter import Toplevel, Button
from creational.abstactfactory import *


class Extra(Toplevel):

    def __init__(self):
        super().__init__()
        self.title('EQs')
        self.geometry('640x480')
        self.button = Button(self, text='Show EQs', command=self.show_eqs)
        self.button.pack(expand=True)

    def show_eqs(self):
        eqs_factory = EQsFactory()
        eqs = eqs_factory.eqs

        for e in eqs:
            self.button = Button(self, text=f'{e.name}')
            self.button.pack(expand=True)