from .base import BaseNatural

class MUL_ND_N:
    def MUL_ND_N(self: BaseNatural, d: int) -> BaseNatural:
        """
        Умножение натурального числа на цифру d.
        Автор: Карпов Андрей гр. 4382
        Возвращает новый объект того же класса.
        """
        # Проверки типа и диапазона
        if not isinstance(d, int):
            raise TypeError("d must be int")
        if d < 0 or d > 9:
            raise ValueError("d must be in 0..9 (digit)")

        # Быстрые случаи
        if d == 0:
            return self.__class__([0])
        if d == 1:
            return self.copy()
        if len(self.digits) == 1 and self.digits[0] == 0:
            # Само число ноль
            return self.__class__([0])

        res_rev = []  # результат в обратном порядке
        carry = 0  # перенос, который передаётся в следующий разряд

        for x in reversed(self.digits):
            prod = x * d + carry
            current_digit = prod % 10
            carry = prod // 10
            res_rev.append(current_digit)

        while carry > 0:
            res_rev.append(carry % 10)
            carry //= 10

        res = list(reversed(res_rev))

        return self.__class__(res)
