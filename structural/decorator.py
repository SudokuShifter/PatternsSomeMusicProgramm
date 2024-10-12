"""
Декоратор — структурный шаблон проектирования,
который позволяет динамически подключать к объекту дополнительную функциональность.
"""


class Entity:
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        return self.sound


class EQ(Entity):
    def __init__(self, eqed):
        self.eqed = eqed

    def play(self):
        return 'EQ[{}]'.format(self.eqed.play())


class Compressor(Entity):
    def __init__(self, compressed):
        self.compressed = compressed

    def play(self):
        return 'Compressor[{}]'.format(self.compressed.play())

