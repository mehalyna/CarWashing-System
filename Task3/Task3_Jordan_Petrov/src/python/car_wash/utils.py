class SingletonMeta(type):

    """
    Singleton metaclass for classes that should only have one instance.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls.__name__] = instance
        return cls._instances[cls.__name__]
