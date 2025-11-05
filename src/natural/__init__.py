from .base import BaseNatural
from .com_nn_d import COM_NN_D

class Natural(
    BaseNatural,
    COM_NN_D
):
    """Класс натурального числа"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']
