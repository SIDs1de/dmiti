from .base_integer import Integer
from .abs_z_n import abs_z_n
from .poz_z_d import poz_z_d

class Integer(
    Integer,
    abs_z_n,
    poz_z_d
):
    """Полный класс целого числа с базовыми методами"""
    pass

__all__ = ['Integer']