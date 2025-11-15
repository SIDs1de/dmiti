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
        zero_rational = Rational(Integer(0, Natural([0])), Natural([1]))
        result = self.__class__([zero_rational])
        
        n = len(self.coefficients) - 1  # Степень текущего многочлена
        
        for i in range(len(self.coefficients)):
            term = other.MUL_PQ_P(self.coefficients[i])
            
            # Правильное вычисление степени: n - i
            power = Natural([n - i])
            term = term.MUL_Pxk_P(power)
            
            result = result.ADD_PP_P(term)
        
        return result