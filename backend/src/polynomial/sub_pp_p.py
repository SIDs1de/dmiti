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
        # Вычитание: self - other = self + (-1) * other
        minus_one = Rational(Integer(1, Natural([1])), Natural([1]))  # -1/1
        return self.ADD_PP_P(other.MUL_PQ_P(minus_one))
