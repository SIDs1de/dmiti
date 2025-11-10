from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational
from typing import Self

class INT_Q_B:
    def INT_Q_B(self) -> bool:
        """
        Проверка сокращенного дробного на целое.
        Если рациональное число является целым, то «да», иначе «нет»
        
        Автор: Дубровский Илья гр.4383
        """
        
        # Если числитель равен 0 - это целое число (0)
        if self.numerator.is_zero():
            return True
            
        # Если знаменатель равен 1 - это целое число
        if (len(self.denominator.digits) == 1 and 
            self.denominator.digits[0] == 1):
            return True
            
        # Во всех остальных случаях - не целое число
        return False