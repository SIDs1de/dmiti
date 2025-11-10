from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational
from typing import Self

class DIV_QQ_Q:
    def DIV_QQ_Q(self, second: Self) -> Self:
        """
        Деление двух рациональных чисел.
        Делитель не равен нулю.
        """

        if second.numerator.is_zero():
            raise ZeroDivisionError("Деление на нулевую дробь невозможно")

        # Числитель: a * d
        numerator = self.numerator.mul_zz_z(
            BaseInteger(0, second.denominator)
        )

        # Знаменатель: b * |c|
        denominator = self.denominator.MUL_NN_N(
            second.numerator.absolute
        )

        # Если делитель отрицательный — меняем знак числителя
        if second.numerator.sign == 1:
            numerator = numerator.mul_zm_z()

        return self.__class__(numerator, denominator)