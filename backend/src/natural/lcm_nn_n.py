from typing import Self

class LCM_NN_N:
    def LCM_NN_N(self: Self, other: Self) -> Self:
        """
        Метод нахождения НОК двух натуральных чисел.
        Результат - натуральное число
        Автор: Рубан Егор гр. 4383
        """

        G = self.GCF_NN_N(other)
        P = self.MUL_NN_N(other)
        L = P.DIV_NN_N(G)

        return L

