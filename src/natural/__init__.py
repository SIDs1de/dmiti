from .base import BaseNatural
from .com_nn_d import COM_NN_D
from .mul_nd_n import MUL_ND_N 

class Natural(
    BaseNatural,
    COM_NN_D,
    MUL_ND_N
):
    """Класс натурального числа"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']
