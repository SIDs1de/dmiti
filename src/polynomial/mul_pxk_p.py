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
        
        k_value = int(''.join(map(str, k.digits)))
        
        # Создаем новый объект того же класса
        result = self.__class__()
        
        # Вручную устанавливаем коэффициенты без валидации
        new_coefficients = []
        
        # Добавляем k нулей
        zero_coeff = Rational(Integer(0, Natural([0])), Natural([1]))
        for _ in range(k_value):
            new_coefficients.append(zero_coeff)
        
        # Добавляем исходные коэффициенты
        new_coefficients.extend(self.coefficients)
        
        # Устанавливаем коэффициенты напрямую
        result.coefficients = new_coefficients
        return result