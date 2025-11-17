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

        # Складываем коэффициенты по позиции через ADD_QQ_Q
        result_coeffs = self.coefficients.copy()
        for index, coefficient in other.coefficients.items():
            if index not in result_coeffs:
                result_coeffs[index] = deepcopy(coefficient)
                continue
            result_coeffs[index] = result_coeffs[index].ADD_QQ_Q(coefficient)

        # Создаём новый полином и удаляем ведущие нули
        result = self.__class__(result_coeffs)

        return result
