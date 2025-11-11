from typing import Self
from copy import deepcopy
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural

class SUB_PP_P:
    def SUB_PP_P(self, other: Self) -> Self:
        """
        Метод вычитания многочленов
        Результат - многочлен
        Автор: Рубан Егор гр. 4383
        """
        coeffs_self = deepcopy(self.coefficients)
        coeffs_other = deepcopy(other.coefficients)

        len_diff = len(coeffs_self) - len(coeffs_other)
        zero_rat = Rational(Integer(0, Natural([0])), Natural([1]))

        if len_diff > 0:
            coeffs_other = [zero_rat] * len_diff + coeffs_other
        elif len_diff < 0:
            coeffs_self = [zero_rat] * (-len_diff) + coeffs_self

        result_coeffs = []
        for a, b in zip(coeffs_self, coeffs_other):
            c = a.SUB_QQ_Q(b)
            result_coeffs.append(c)

        result = self.__class__(result_coeffs)
        result._validate()
        return result