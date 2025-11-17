from .enums import BoolResult
from typing import Self

class GCF_NN_N:
    def GCF_NN_N(self: Self, other: Self) -> Self:
        """
        Метод нахождения НОД двух натуральных чисел.
        Результат - натуральное число.
        Автор: Рубан Егор гр. 4383
        """

        if self.COM_NN_D(other) == 1:
            self, other = other, self

        while other.NZER_N_B() == BoolResult.YES:
            comp = self.COM_NN_D(other)
            if comp == 0:
                return self
            elif comp == 1:
                self, other = other, self

            R = self.MOD_NN_N(other)
            self, other = other, R

        return self


