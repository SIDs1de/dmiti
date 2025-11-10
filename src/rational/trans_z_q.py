from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational
from typing import Self

class TRANS_Z_Q:
    def TRANS_Z_Q(self, integer: BaseInteger) -> BaseRational:
        """
        Преобразование целого в дробное
        
        Автор: Дубровский Илья гр.4383
        """
        # Целое число преобразуется в дробь с знаменателем 1
        denominator = BaseNatural([1])
        return BaseRational(integer, denominator)