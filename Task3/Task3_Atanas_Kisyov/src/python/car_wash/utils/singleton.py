"""Singleton design pattern definition"""
class Singleton(type):

    """Base class to limit pools to one"""

    _instance = {}

    def __new__(cls, *args, **kwargs):
        """Create an instance only on first call"""

        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instance[cls]
