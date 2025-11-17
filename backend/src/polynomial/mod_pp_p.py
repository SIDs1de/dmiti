from typing import Self
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural


class MOD_PP_P:
    def MOD_PP_P(self: Self, other: Self) -> Self:
        """
        Остаток от деления многочлена на многочлен при делении с остатком
        Возвращает остаток от деления self на other
        Автор: Королев Семен, гр. 4382
        """
        # Проверка деления на нулевой многочлен
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")

        # Если делимое нулевое, возвращаем нулевой многочлен
        if self.is_zero():
            return self.copy()

        # Вычисляем частное
        quotient = self.DIV_PP_P(other)

        # Вычисляем произведение делителя на частное
        divisor_times_quotient = other.MUL_PP_P(quotient)

        # Вычисляем остаток: self - divisor_times_quotient
        remainder = self.SUB_PP_P(divisor_times_quotient)

        return remainder