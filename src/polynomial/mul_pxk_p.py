from src.natural import Natural
from src.integer import Integer
from src.rational import Rational
from typing import Self

class MUL_Pxk_P:
    def MUL_Pxk_P(self: Self, k: Natural) -> Self:
        """
        Умножение многочлена на x^k, k-натуральное или 0
        """
        if k.digits == [0]:
            return self.__class__(self.coefficients.copy())
        
        # В формате "старшая степень первая" добавляем нули в конец
        new_coefficients = {}
        
        # Добавляем k нулей в конец
        for index, coeff in self.coefficients.items():
            new_coefficients[index + int(str(k))] = coeff
        
        # Устанавливаем коэффициенты напрямую
        result = self.__class__(new_coefficients)
        return result