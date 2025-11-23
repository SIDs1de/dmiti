from typing import Self
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural

class FAC_P_Q:
    def FAC_P_Q(self: Self) -> Rational:
        """
        Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей.
        Автор: Карпов Андрей гр. 4382
        Возвращает Rational(НОД/НОК).
        """
        gcf_num: Natural | None = None # НОД числителей
        lcm_den: Natural | None = None # НОК знаменателей

        for coeff in self.coefficients.values(): # Проходим по всем коэффициентам многочлена
            if coeff.numerator.poz_z_d() == 0: # Пропускаем нулевые коэффициенты
                continue

            abs_num = coeff.numerator.abs_z_n() # Абсолютное значение числителя
            den = coeff.denominator # Знаменатель коэффициента

            # Первые ненулевые значения инициализируют процесс
            if gcf_num is None:
                gcf_num = abs_num
                lcm_den = den
            else:
                gcf_num = gcf_num.GCF_NN_N(abs_num) # Находим НОД
                lcm_den = lcm_den.LCM_NN_N(den) # Находим НОК

        # Если все коэффициенты равны нулю — возвращаем 1/1
        if gcf_num is None:
            one_int = Integer(0, Natural([1])) # Создаём целое число 1
            return Rational(one_int, Natural([1])) # Возвращаем рациональное число 1/1
        
        gcf_int = gcf_num.trans_n_z()
        return Rational(gcf_int, lcm_den)
