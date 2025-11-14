from typing import Self
from copy import deepcopy
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural

class ADD_PP_P:
    def ADD_PP_P(self, other: Self) -> Self:
        """
        Метод сложения двух полиномов.
        Коэффициенты выравниваются по степени.
        Результат - новый полином.
        Автор: Алиев Вусал, гр. 4383
        """
        zero_rat = Rational(Integer(0, Natural([0])), Natural([1]))

        # Определяем максимальную степень
        max_degree = max(self.m, other.m)

        # Выровненные коэффициенты от старшей к младшей степени
        coeffs_self_aligned = [zero_rat] * (max_degree - self.m) + deepcopy(self.coefficients)
        coeffs_other_aligned = [zero_rat] * (max_degree - other.m) + deepcopy(other.coefficients)

        # Складываем коэффициенты по позиции через ADD_QQ_Q
        result_coeffs = [a.ADD_QQ_Q(b) for a, b in zip(coeffs_self_aligned, coeffs_other_aligned)]

        # Создаём новый полином и удаляем ведущие нули
        result = self.__class__(result_coeffs)
        result._validate()

        return result
