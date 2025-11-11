from typing import Self
from src.natural import Natural


class DEG_P_N:
    def DEG_P_N(self: Self) -> Natural:
        """
        Возвращает степень многочлена
        Автор: Королев Семен гр. 4382
        """
        degree = len(self.coefficients) - 1

        if degree == 0:
            return Natural([0])

        digits = []
        temp = degree
        while temp > 0:
            digits.insert(0, temp % 10)
            temp //= 10

        return Natural(digits)