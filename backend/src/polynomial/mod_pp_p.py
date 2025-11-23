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
        # Базовое назначение: вычисляет остаток от деления многочленов через частное и вычитание

        if other.is_zero():  # Проверка деления на ноль
            raise ZeroDivisionError("Деление на нулевой многочлен")

        if self.is_zero():  # Нулевой многочлен в остатке
            return self.copy()

        quotient = self.DIV_PP_P(other)  # Частное от деления
        divisor_times_quotient = other.MUL_PP_P(quotient)  # Делитель * частное
        remainder = self.SUB_PP_P(divisor_times_quotient)  # Остаток = делимое - произведение

        return remainder