from tkinter import *
from structural.adapter import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Conwerter window')
        self.geometry('640x480')

        self.button = Button(self, text='Audio Record', command=self.audio)
        self.button.pack(expand=True)

        self.button2 = Button(self, text='Midi', command=self.midi)
        self.button2.pack(expand=True)

    def audio(self):
        track = AudioTrack()
        track.audio_record()

    def midi(self):
        track = AudioToMidiAdapter()
        track.audio_record()