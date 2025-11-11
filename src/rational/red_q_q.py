from typing import Self
from src.natural import Natural
from src.integer import Integer


class RED_Q_Q:
    def RED_Q_Q(self: Self) -> Self:
        """
        Сокращение дроби
        Автор: Королев Семен гр. 4382
        """

        if self.numerator.is_zero():
            return self.__class__(Integer(0, Natural([0])), Natural([1]))

        abs_numerator = self.numerator.abs_z_n()

        gcd = abs_numerator.GCF_NN_N(self.denominator)

        new_numerator = self.numerator.div_zz_z(Integer(0, gcd))
        new_denominator = self.denominator.DIV_NN_N(gcd)

        return self.__class__(new_numerator, new_denominator)