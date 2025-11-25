from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational
from typing import Self

class MUL_QQ_Q:
    def MUL_QQ_Q(self, second: Self) -> Self:
        """
        Умножение двух рациональных чисел.
        Результат - рациональное число
        Автор: Рубан Егор гр.4383
        """

        # Умножаем числители двух рациональных чисел
        # mul_zz_z выполняет умножение целых чисел и возвращает целое число
        numerator = self.numerator.mul_zz_z(second.numerator)

        # Умножаем знаменатели
        # MUL_NN_N выполняет умножение натуральных чисел
        denominator = self.denominator.MUL_NN_N(second.denominator)

        # Формируем новое рациональное число из полученного числителя и знаменателя
        result = self.__class__(numerator, denominator)

        # Сокращаем результат
        # RED_Q_Q приводит рациональное число к несократимому виду
        return result.RED_Q_Q()

