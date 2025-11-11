from src.integer import Integer
from src.natural import Natural
from typing import Self

class TRANS_Z_Q:
    def TRANS_Z_Q(self: Self, integer: Integer) -> Self:
        """
        Преобразование целого в дробное
        
        Автор: Дубровский Илья гр.4383
        """
        # Целое число преобразуется в дробь с знаменателем 1
        denominator = Natural([1])
        return self.__class__(integer, denominator)