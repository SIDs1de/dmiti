from typing import Self
from src.natural import Natural
from src.integer import Integer
from src.rational import Rational

class MUL_PP_P:
    def MUL_PP_P(self: Self, other: Self) -> Self:
        """
        Умножение многочленов
        Автор: Свинцов Егор гр. 4383
        
        Математическая формула:
        Если P(x) = ∑aᵢxⁱ и Q(x) = ∑bⱼxʲ, то
        P(x) × Q(x) = ∑(aᵢ × bⱼ)xⁱ⁺ʲ
        """
        # Начинаем с нулевого многочлена: R(x) = 0
        result = self.__class__()
        
        # Для каждого слагаемого aᵢxⁱ из первого многочлена
        for i, coeff in self.coefficients.items():
            # Умножаем второй многочлен на коэффициент aᵢ: Q(x) × aᵢ
            term = other.MUL_PQ_P(coeff)
            
            # Умножаем на xⁱ
            if i == 0:
                power = Natural([0])  # x⁰ = 1
            else:
                # Преобразуем степень i в натуральное число
                digits = [] # Список цифр числа i
                temp = i
                while temp > 0:
                    digits.insert(0, temp % 10)
                    temp //= 10
                power = Natural(digits)
            term = term.MUL_Pxk_P(power)  # Умножаем на xⁱ
            
            # Добавляем к результату: R(x) += aᵢ × Q(x) × xⁱ
            result = result.ADD_PP_P(term)
        
        # Возвращаем итоговый многочлен R(x) = P(x) × Q(x)
        return result