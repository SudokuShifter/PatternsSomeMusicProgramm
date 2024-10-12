from tkinter import *
from creational.singleton import Singleton
import eqswindow
import footerwindow
import conwerterwindow
import decoratorwindow
import renderwindow


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

        self.button4 = Button(self, text='decorator play', command=self.decorator_play)
        self.button4.pack(expand=True)

        self.button5 = Button(self, text='export', command=self.create_export)
        self.button5.pack(expand=True)

    def create_window_eqs(self):
        global extra_window
        extra_window = eqswindow.Extra()

    def create_footer_eqs(self):
        global extra_window
        extra_window = footerwindow.Extra()

    def create_audio(self):
        global extra_window
        extra_window = conwerterwindow.Extra()

    def decorator_play(self):
        global extra_window
        extra_window = decoratorwindow.Extra()

    def create_export(self):
        global extra_window
        extra_window = renderwindow.Extra()

    def __init__(self):
        print('calling from __init__')