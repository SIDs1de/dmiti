from typing import Self
from .enums import BoolResult

class NZER_N_B:
    def NZER_N_B(self: Self) -> BoolResult:
        """
        Проверка на ноль
        Автор: Королев Семен гр. 4382
        Возвращает:
        BoolResult.YES - если число не равно 0
        BoolResult.NO - если число равно 0
        """
        if len(self.digits) == 1 and self.digits[0] == 0:
            return BoolResult.NO
        else:
            return BoolResult.YES