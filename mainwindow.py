from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow
import conwerterwindow

class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()
        self.button = Button(self, text='open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

        self.button2 = Button(self, text='open footer', command=self.create_footer_eqs)
        self.button2.pack(expand=True)

        self.button3 = Button(self, text='audio play', command=self.create_audio)
        self.button3.pack(expand=True)

    def create_window_eqs(self):
        global extra_window
        extra_window = eqswindow.Extra()

    def create_footer_eqs(self):
        global extra_window
        extra_window = footerwindow.Extra()

    def create_audio(self):
        global extra_window
        extra_window = conwerterwindow.Extra()

    def __init__(self):
        print('calling from __init__')