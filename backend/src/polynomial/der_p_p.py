from typing import Self
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural

class DER_P_P:
    def DER_P_P(self) -> Self:
        """
        Метод нахождения производной многочлена
        Результат - многочлен
        Автор: Рубан Егор гр. 4383
        """
        n = self.m

        if n == 0:
            zero = Rational(Integer(0, Natural([0])), Natural([1]))
            return self.__class__({0: zero})

        new_coeffs = {}

        for i, coef in self.coefficients.items():
            # Пропускаем константные члены (i == 0), так как их производная равна 0
            if i == 0:
                continue
            
            degree = i - 1
            rat_degree = Rational(Integer(0, Natural([i])), Natural([1]))

            new_coef = coef.MUL_QQ_Q(rat_degree)
            new_coeffs[degree] = new_coef

        return self.__class__(new_coeffs)