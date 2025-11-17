from typing import Self
from src.natural import Natural
from src.integer import Integer
from src.rational import Rational

class MUL_PP_P:
    def MUL_PP_P(self: Self, other: Self) -> Self:
        """
        Умножение многочленов
        Автор: Свинцов Егор гр. 4383
        """
        result = self.__class__()
        
        for i, coeff in self.coefficients.items():
            term = other.MUL_PQ_P(coeff)
            
            # Сдвиг на степень i (индекс = степень)
            if i == 0:
                power = Natural([0])
            else:
                digits = []
                temp = i
                while temp > 0:
                    digits.insert(0, temp % 10)
                    temp //= 10
                power = Natural(digits)
            term = term.MUL_Pxk_P(power)
            
            result = result.ADD_PP_P(term)
        
        return result