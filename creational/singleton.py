class Singleton(object):
    """
    Singleton - это паттерн проектирования из категории создания объектов,
    его смысл в том, чтобы создать 1 единственный экземпляр объекта на весь проект,
    и все кто с ним взаимодействует - должны использовать лишь 1 инстанс этого объекта
    """
    def __new__(cls, *args, **kwargs):
        it = cls.__dict__.get('__it__')
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwargs)
        print('calling from __new__')
        return it

    def init(self, *args, **kwargs):
        pass