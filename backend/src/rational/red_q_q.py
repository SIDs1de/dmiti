from typing import Self
from src.natural import Natural
from src.integer import Integer


class RED_Q_Q:
    def RED_Q_Q(self: Self) -> Self:
        """
        Сокращение дроби
        Автор: Королев Семен гр. 4382
        """
        # Базовое назначение: сокращает дробь через НОД числителя и знаменателя

        if self.numerator.is_zero():  # Нулевой числитель - возврат 0/1
            return self.__class__(Integer(0, Natural([0])), Natural([1]))

        abs_numerator = self.numerator.abs_z_n()  # Модуль числителя для НОД
        gcd = abs_numerator.GCF_NN_N(self.denominator)  # Вычисление НОД

        new_numerator = self.numerator.div_zz_z(Integer(0, gcd))  # Деление числителя на НОД
        new_denominator = self.denominator.DIV_NN_N(gcd)  # Деление знаменателя на НОД

        return self.__class__(new_numerator, new_denominator)  # Новая сокращенная дробь