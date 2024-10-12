from abc import ABCMeta, abstractmethod


class Plugin(metaclass=ABCMeta):
    """
    это порождающий шаблон проектирования,
    предоставляющий подклассам (дочерним классам, субклассам)
    интерфейс для создания экземпляров некоторого класса.
    """
    @abstractmethod
    def type(self):
        raise NotImplementedError


class EffectPlugin(Plugin):

    def __init__(self):
        self.type = 'Effect'

    def type(self):
        return self.type


class SynthPlugin(Plugin):
    def __init__(self):
        self.type = 'Synth'

    def type(self):
        return self.type


class Creator:

    @staticmethod
    def factory(type):
        if type == 'Effect':
            return EffectPlugin()
        elif type == 'Synth':
            return SynthPlugin()
        return None
