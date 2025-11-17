from .base_integer import BaseInteger
from .abs_z_n import Abs_z_n
from .poz_z_d import Poz_z_d
from .mul_zm_z import Mul_zm_z
from .trans_z_n import Trans_z_n
from .mul_zz_z import Mul_zz_z
from .add_zz_z import Add_zz_z
from .sub_zz_z import Sub_zz_z
from .div_zz_z import Div_zz_z
from .mod_zz_z import MOD_ZZ_Z

class Integer(
    BaseInteger,
    Abs_z_n,
    Poz_z_d,
    Mul_zm_z,
    Div_zz_z,
    Trans_z_n,
    Mul_zz_z,
    Add_zz_z,
    Sub_zz_z,
    MOD_ZZ_Z
):
    """Класс целого числа"""
    pass

__all__ = ['Integer']
