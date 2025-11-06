from typing import cast
from .base import BaseNatural


class DIV_NN_DK:
    def DIV_NN_DK(self: BaseNatural, second: BaseNatural, k: int) -> int:
        """
        Автор: Viktor Permitin
        Алгоритм Макана:
        Вычисление первой цифры деления
        большего натурального на меньшее,
        домноженное на 10^k,где k - номер
        позиции этой цифры (номер считается
        с нуля)

        """
        if k < 0:
            raise ValueError("k must be non-negative")
        if len(second.digits) == 1 and second.digits[0] == 0:
            raise ValueError("division by zero")

        shifted = second.MUL_Nk_N(k)

        if self.COM_NN_D(shifted) == 1:
            return 0

        low, high = 0, 9
        best = 0
        while low <= high:
            mid = (low + high) // 2
            candidate = shifted.MUL_ND_N(mid)
            cmp = self.COM_NN_D(candidate)
            if cmp == 2 or cmp == 0:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best
