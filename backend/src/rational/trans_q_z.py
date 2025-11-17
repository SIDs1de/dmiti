from src.integer import Integer
from typing import Self

class TRANS_Q_Z:
    def TRANS_Q_Z(self: Self) -> Integer:
        """
        Преобразование сокращенного дробного в целое (если знаменатель равен 1)
        
        Автор: Дубровский Илья гр.4383
        """
        # Проверяем, что знаменатель равен 1 (дробь является целым числом)
        if len(self.denominator.digits) == 1 and self.denominator.digits[0] == 1:
            return self.numerator
        else:
            raise ValueError("Дробь не является целым числом (знаменатель ≠ 1)")