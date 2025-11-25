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
        Базовое назначение: вычисляет производную многочлена по стандартным правилам дифференцирования
        """
        # Вычисляет производную многочлена, умножая каждый коэффициент на его степень и уменьшая степени на 1
        # Получаем степень многочлена
        n = self.m

        # Константа → производная 0
        if n == 0:
            zero = Rational(Integer(0, Natural([0])), Natural([1]))
            return self.__class__({0: zero})

        # Словарь для коэффициентов производной
        new_coeffs = {}

        # Для каждого члена многочлена: коэффициент умножается на степень, степень уменьшается на 1
        for i, coef in self.coefficients.items():
            # Пропуск константы (производная = 0)
            if i == 0:
                continue

            # Новая степень = i-1
            degree = i - 1

            # Преобразование степени i в натуральное число для умножения
            digits = []
            temp = i
            while temp > 0:
                digits.insert(0, temp % 10)
                temp //= 10
            power = Natural(digits)

            # Создание рационального числа из степени i
            rat_degree = Rational(Integer(0, power), Natural([1]))

            # Умножение коэффициента на степень: coef * i
            new_coef = coef.MUL_QQ_Q(rat_degree)

            # Сохранение нового коэффициента
            new_coeffs[degree] = new_coef

        # Возврат нового многочлена - производной
        return self.__class__(new_coeffs)