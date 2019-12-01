def raise_exception(ex: Exception):
    raise ex


class Settings:
    _instance = None

    def __new__(cls, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, debug_mode=None, path=''):
        params = {
            k: v for k, v in locals().items()
            if k != 'self' and not hasattr(self.__class__, k)
        }
        for k, v in params.items():
            ex = TypeError(f'{k} attribute cannot be assigned')
            setattr(self, f'_{k}', v)
            setattr(self.__class__, k, property(
                lambda o, name=k: getattr(o, f'_{name}'),
                lambda o, v, name=k: raise_exception(ex),
            ))

    @classmethod
    def clear(cls):
        cls._instance = None
        props = {k for k, v in cls.__dict__.items() if isinstance(v, property)}
        for name in props:
            delattr(cls, name)
