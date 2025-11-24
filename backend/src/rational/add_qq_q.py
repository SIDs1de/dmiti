from typing import Self

class ADD_QQ_Q:
    def ADD_QQ_Q(self: Self, other: Self) -> Self:
        """
        Сложение дробей
        Автор: Свинцов Егор гр. 4383
        
        Математическая формула:
        a/b + c/d = (a × (НОК(b,d)/b) + c × (НОК(b,d)/d)) / НОК(b,d)
        """
        # Находим общий знаменатель: НОК(denom1, denom2)
        common_denominator = self.denominator.LCM_NN_N(other.denominator)

        # Вычисляем дополнительные множители для числителей:
        # factor1 = НОК(b,d) / b, factor2 = НОК(b,d) / d
        factor1 = common_denominator.DIV_NN_N(self.denominator)
        factor2 = common_denominator.DIV_NN_N(other.denominator)
        
        # Преобразуем натуральные множители в целые числа (положительные)
        factor1_int = factor1.trans_n_z()
        factor2_int = factor2.trans_n_z()
        
        # Умножаем числители на соответствующие множители:
        # numerator1 = a × factor1, numerator2 = c × factor2
        numerator1 = self.numerator.mul_zz_z(factor1_int)
        numerator2 = other.numerator.mul_zz_z(factor2_int)
        
        # Складываем числители: total_numerator = a×factor1 + c×factor2
        total_numerator = numerator1.add_zz_z(numerator2)
        
        # Возвращаем новую дробь и сокращаем её: (a×factor1 + c×factor2) / НОК(b,d)
        return self.__class__(total_numerator, common_denominator).RED_Q_Q()