from .base import Natural
from .com_nn_d import COM_NN_D

class Natural(
    Natural,
    COM_NN_D
):
    """Класс натурального числа"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']
