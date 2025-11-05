from .base import BaseNatural
from .add_1n_n import ADD_1N_N

class Natural(
    BaseNatural,
    ADD_1N_N
):
    """Класс натурального числа"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']