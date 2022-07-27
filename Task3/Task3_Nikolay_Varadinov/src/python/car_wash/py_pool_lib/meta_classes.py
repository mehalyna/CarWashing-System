"""Meta classes"""


class SingletonMeta(type):

    """Singleton Meta class. After first initialization of an instance
       in its classes, any new changes to __init__ won't have effect on the
       the returned instance.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
