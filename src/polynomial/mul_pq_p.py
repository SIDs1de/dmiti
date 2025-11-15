from typing import Self
from src.rational import Rational


class MUL_PQ_P:
    def MUL_PQ_P(self: Self, second: Rational) -> Self:
        """
        Приготовил: Permitin Viktor
        Умножение многочлена на рациональное число
        """
        result = self.copy()

        for index, coefficient in self.coefficients.items():
            result.coefficients[index] = coefficient.MUL_QQ_Q(second)

        return result
