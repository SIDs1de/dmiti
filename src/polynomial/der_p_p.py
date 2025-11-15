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

        if  n == 0:
            zero = Rational(Integer(0, Natural([0])), Natural([1]))
            return self.__class__([zero])

        new_coeffs = []

        for i, coef in enumerate(self.coefficients):
            degree = n - i
            if degree == 0:
                continue

            rat_degree = Rational(Integer(0, Natural([degree])), Natural([1]))

            new_coef = coef.MUL_QQ_Q(rat_degree)
            new_coeffs.append(new_coef)

        return self.__class__(new_coeffs)