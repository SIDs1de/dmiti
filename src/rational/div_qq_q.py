from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational
from typing import Self

class DIV_QQ_Q:
    def DIV_QQ_Q(self, second: Self) -> Self:
        """
        Деление двух рациональных чисел.
        Делитель не равен нулю.
        Автор: Алиев Вусал гр.4383
        """

        if second.numerator.is_zero():
            raise ZeroDivisionError("Деление на нулевую дробь невозможно")

        numerator = self.numerator.mul_zz_z(
            BaseInteger(0, second.denominator)
        )

        denominator = self.denominator.MUL_NN_N(
            second.numerator.absolute
        )

        if second.numerator.sign == 1:
            numerator = numerator.mul_zm_z()

        return self.__class__(numerator, denominator)