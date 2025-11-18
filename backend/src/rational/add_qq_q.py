from typing import Self

class ADD_QQ_Q:
    def ADD_QQ_Q(self: Self, other: Self) -> Self:
        """
        Сложение дробей
        Автор: Свинцов Егор гр. 4383
        """
        # Находим общий знаменатель
        common_denominator = self.denominator.LCM_NN_N(other.denominator)

        # Вычисляем дополнительные множители для числителей
        factor1 = common_denominator.DIV_NN_N(self.denominator)
        factor2 = common_denominator.DIV_NN_N(other.denominator)
        
        # Преобразуем натуральные множители в целые числа
        factor1_int = factor1.trans_n_z()
        factor2_int = factor2.trans_n_z()
        
        # Умножаем числители на соответствующие множители
        numerator1 = self.numerator.mul_zz_z(factor1_int)
        numerator2 = other.numerator.mul_zz_z(factor2_int)
        
        # Складываем числители
        total_numerator = numerator1.add_zz_z(numerator2)
        
        # Возвращаем новую дробь
        return self.__class__(total_numerator, common_denominator).RED_Q_Q()