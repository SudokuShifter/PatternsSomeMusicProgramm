class EQsFactory:
    """
    Порождающий шаблон проектирования, который предоставляет интерфейс
    для создания семейств взаимосвязанных или взаимозависимых объектов, не специфицируя их конкретных классов
    """
    def __init__(self):
        self._eqsfactory = [FabFilter(5, 'Pro Q'),
                            UAD(4, 'UAD'),
                            Waves(10, 'Waves')]

    @property
    def eqs(self):
        return self._eqsfactory


class EQ:
    def __init__(self, bands, name):
        self.bands = bands
        self.name = name

    def get_bands(self):
        return self.bands


class FabFilter(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def get_bands(self):
        return super().get_bands()


class UAD(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def get_bands(self):
        return super().get_bands()


class Waves(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def get_bands(self):
        return super().get_bands()