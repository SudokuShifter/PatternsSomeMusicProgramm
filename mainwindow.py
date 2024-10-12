from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow


class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()
        self.button = Button(self, text='open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

        self.button2 = Button(self, text='open footer', command=self.create_footer_eqs)
        self.button2.pack(expand=True)

    def create_window_eqs(self):
        global extra_window
        extra_window = eqswindow.Extra()

    def create_footer_eqs(self):
        global extra_window
        extra_window = footerwindow.Extra()

    def __init__(self):
        print('calling from __init__')