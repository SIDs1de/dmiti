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

        # Создаём рациональное число -1
        # Integer(1, Natural([1])) — целое число со знаком 1 (минус) и модулем 1
        # Natural([1]) — знаменатель 1
        minus_one = Rational(Integer(1, Natural([1])), Natural([1]))  # -1/1

        # Вычитание многочленов сводим к сложению:
        #   self - other = self + (-1) * other
        # MUL_PQ_P — умножение многочлена на рациональное число
        # ADD_PP_P — сложение многочленов
        return self.ADD_PP_P(other.MUL_PQ_P(minus_one))
