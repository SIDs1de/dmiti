from .base import BaseNatural
from .com_nn_d import COM_NN_D
from .nzer_n_b import NZER_N_B

class Natural(
    BaseNatural,
    COM_NN_D,
    NZER_N_B
):
    """Класс натурального числа"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']
