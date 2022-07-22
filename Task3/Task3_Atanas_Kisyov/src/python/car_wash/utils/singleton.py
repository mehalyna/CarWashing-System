"""Singleton design pattern definition"""
class Singleton:

    """Base class to limit pools to one"""

    _instance = None

    def __new__(cls, *args: tuple, **kwargs: dict):
        """Create an instance only on first call"""

        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
