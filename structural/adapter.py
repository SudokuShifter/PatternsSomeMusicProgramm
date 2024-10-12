from abc import ABC, abstractmethod


class Audio(ABC):
    @abstractmethod
    def audio_record(self):
        pass


class Midi(ABC):
    @abstractmethod
    def midi_track(self):
        pass


class AudioTrack(Audio):
    def audio_record(self):
        print('Audio is playing')


class MidiTrack(Midi):
    def midi_track(self):
        print('Midi is playing')


class AudioToMidiAdapter(Audio):
    def __init__(self):
        self.midi = MidiTrack()

    def audio_record(self):
        self.midi.midi_track()
