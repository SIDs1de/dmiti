from typing import Self
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural


class DIV_PP_P:
    def DIV_PP_P(self: Self, other: Self) -> Self:
        """
        Деление многочлена на многочлен с остатком (частное)
        Возвращает частное от деления self на other
        Автор: Алиев Вусал, гр. 4383
        """
        # Проверка деления на нулевой многочлен
        if other.is_zero():
            raise ZeroDivisionError("Деление на нулевой многочлен")

        # Если делимое нулевое, возвращаем нулевой многочлен
        if self.is_zero():
            return self.copy()

        # Создаем копии многочленов для работы
        dividend = self.copy()
        divisor = other.copy()

        # Инициализируем частное как нулевой многочлен
        zero_rational = Rational(Integer(0, Natural([0])), Natural([1]))
        quotient = self.__class__({0: zero_rational})

        # Получаем степени многочленов
        deg_dividend = dividend.DEG_P_N()
        deg_divisor = divisor.DEG_P_N()
        deg_dividend_int = int(str(deg_dividend))
        deg_divisor_int = int(str(deg_divisor))

        # Если степень делителя больше степени делимого, возвращаем нулевой многочлен
        if deg_divisor_int > deg_dividend_int:
            return quotient

        # Алгоритм деления
        while deg_dividend_int >= deg_divisor_int and not dividend.is_zero():
            # Получаем старшие коэффициенты
            lead_coeff_dividend = dividend.coefficients[deg_dividend_int]
            lead_coeff_divisor = divisor.coefficients[deg_divisor_int]

            # Вычисляем коэффициент для текущего члена частного
            current_coeff = lead_coeff_dividend.DIV_QQ_Q(lead_coeff_divisor)

            # Вычисляем степень для текущего члена
            current_degree = deg_dividend_int - deg_divisor_int

            # Создаем текущий член частного
            current_term_coeffs = {0: current_coeff}
            current_term = self.__class__(current_term_coeffs)

            # Умножаем на x^k
            degree_natural = Natural([int(d) for d in str(current_degree)])
            current_term = current_term.MUL_Pxk_P(degree_natural)

            # Добавляем текущий член к частному
            quotient = quotient.ADD_PP_P(current_term)

            # Умножаем делитель на текущий член
            temp1 = divisor.MUL_PQ_P(current_coeff)
            temp = temp1.MUL_Pxk_P(degree_natural)

            # Вычитаем из делимого
            dividend = dividend.SUB_PP_P(temp)

            # Обновляем степень делимого
            deg_dividend = dividend.DEG_P_N()
            deg_dividend_int = int(str(deg_dividend))

        return quotient