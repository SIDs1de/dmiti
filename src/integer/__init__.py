from .base_integer import Integer
from .abs_z_n import Abs_z_n
from .poz_z_d import Poz_z_d

class Integer(
    Integer,
    Abs_z_n,
    Poz_z_d
):
    """Класс целого числа с базовыми методами"""
    pass

__all__ = ['Integer']