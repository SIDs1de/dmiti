from .base import BaseNatural
from .enums import BoolResult
from typing import Self

class GCF_NN_N:
    def GCF_NN_N(self, other: Self) -> Self:
        """
        Метод нахождения НОД двухнатуральных чисел. 
        Результат - натуральное число.
        Автор: Рубан Егор гр. 4383
        """
        A = BaseNatural(self.digits)
        B = BaseNatural(self.digits)

        if A.COM_NN_D(B) == 1:
            A, B = B, A

        while NZER_N_B(B) == BoolResult.YES:
            comp = A.COM_NN_D(B)
            if comp == 0:
                return A
            elif comp == 1:
                A, B = B, A

            R = A.MOD_NN_N(B)
            A, B = B, R

        return A


