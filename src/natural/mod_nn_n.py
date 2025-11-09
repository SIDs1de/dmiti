from .base import BaseNatural

class MOD_NN_N:
    def MOD_NN_N(self, second):
        """
        Остаток от деления первого натурального числа на второе (делитель отличен от нуля)
        Использует: DIV_NN_N, SUB_NDN_N
        """
        if len(second.digits) == 1 and second.digits[0] == 0:
            raise ValueError("division by zero")

        quotient = self.DIV_NN_N(second)
        remainder = self.copy()

        for i in range(len(quotient.digits)):
            d = quotient.digits[i]
            if d == 0:
                continue

            k = len(quotient.digits) - i - 1
            shifted = second.MUL_Nk_N(k)
            remainder = remainder.SUB_NDN_N(shifted, d)

        return remainder
