from .base import BaseNatural


class SUB_NDN_N:
    def SUB_NDN_N(self: BaseNatural, second: BaseNatural, d: int) -> BaseNatural:
        """
        Автор: Viktor Permitin
        Я эгоиист😈😈😈
        Вычитание из натурального другого
        натурального, умноженного на цифру
        """
        if d < 0 or d > 9:
            raise ValueError("d must be in 0..9 (digit)")
        second = second.MUL_ND_N(d)
        cmp_result = second.COM_NN_D(self)
        if cmp_result >= 2:
            raise ValueError("Result must be positive (macan)")
        return self.SUB_NN_N(second)
