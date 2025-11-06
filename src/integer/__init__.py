from .base_integer import BaseInteger
from .abs_z_n import Abs_z_n
from .poz_z_d import Poz_z_d
from .mul_zm_z import Mul_zm_z

class Integer(
    BaseInteger,
    Abs_z_n,
    Poz_z_d,
    Mul_zm_z
):
    """Класс целого числа"""
    pass

__all__ = ['Integer']