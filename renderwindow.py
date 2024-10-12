from tkinter import *
from tkinter.messagebox import askquestion
from structural.facade import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Rendering')
        self.geometry('200x480')

        self.button = Button(self, text='Start rendering', command=self.start_rendering)
        self.button.pack(expand=True)

    def start_rendering(self):
        render_track = Render()
        askquestion('...', message='Start rendering?')
        render_track.start_rendering()