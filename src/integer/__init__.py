from .base_integer import BaseInteger
from .abs_z_n import Abs_z_n
from .poz_z_d import Poz_z_d

class Integer(
    BaseInteger,
    Abs_z_n,
    Poz_z_d
):
    """Класс целого числа"""
    pass

__all__ = ['Integer']