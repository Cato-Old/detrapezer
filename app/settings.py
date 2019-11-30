class Settings:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, debug_mode=None):
        if not hasattr(self, 'debug_mode'):
            self.debug_mode = debug_mode

    @classmethod
    def clear(cls):
        Settings._instance = None
