from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational
from typing import Self

class MUL_QQ_Q:
    def MUL_QQ_Q(self, second: Self) -> Self:
        """
        Умножение двух рациональных чисел.
        Результат - рациональное число
        Автор: Рубан Егор гр.4383
        """

        numerator = self.numerator.mul_zz_z(second.numerator)

        denominator = self.denominator.MUL_NN_N(second.denominator)

        result = self.__class__(numerator, denominator)

        return result

