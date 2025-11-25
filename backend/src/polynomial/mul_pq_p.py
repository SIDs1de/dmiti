from typing import Self
from src.rational import Rational


class MUL_PQ_P:
    def MUL_PQ_P(self: Self, second: Rational) -> Self:
        """
        Приготовил: Permitin Viktor
        Умножение многочлена на рациональное число
        """
        # Умножает рациональное на коэффициенты многочлена
        # Создаем копию исходного многочлена для сохранения его неизменности
        result = self.copy()

        # Проходим по всем коэффициентам многочлена
        # coefficients - словарь, где ключ - степень, значение - коэффициент (Rational)
        for index, coefficient in self.coefficients.items():
            # Умножаем каждый коэффициент на рациональное число second
            # MUL_QQ_Q выполняет умножение двух рациональных чисел
            result.coefficients[index] = coefficient.MUL_QQ_Q(second)

        # Возвращаем многочлен с обновленными коэффициентами
        return result
