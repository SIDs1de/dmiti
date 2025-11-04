from .base import Natural
from typing import Tuple


class NaturalDivision:
    """Методы деления"""

    def sub_ndn_n(self: Natural, other: Natural, digit: int) -> Natural:
        """N-9: Вычитание с умножением"""
        # TODO: Реализовать
        return Natural([0])

    def div_nn_dk(self: Natural, other: Natural) -> Tuple[int, int]:
        """N-10: Первая цифра деления"""
        # TODO: Реализовать
        return (0, 0)

    def div_nn_n(self: Natural, other: Natural) -> Natural:
        """N-11: Неполное частное"""
        # TODO: Реализовать
        return Natural([0])

    def mod_nn_n(self: Natural, other: Natural) -> Natural:
        """N-12: Остаток от деления"""
        # TODO: Реализовать
        return Natural([0])
