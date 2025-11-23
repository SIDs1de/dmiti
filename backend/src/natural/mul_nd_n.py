from typing import Self

class MUL_ND_N:
    def MUL_ND_N(self: Self, d: int) -> Self:
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
        if d == 0: # Если умножаем на 0, то результат всегда 0
            return self.__class__([0]) 
        if d == 1: # Если умножаем на 1, результат остаётся тем же числом
            return self.copy()
        if len(self.digits) == 1 and self.digits[0] == 0: # Если само число равно 0, результат тоже 0
            return self.__class__([0])

        res_rev = []  # результат в обратном порядке
        carry = 0  # перенос, который передаётся в следующий разряд

        for x in reversed(self.digits): # Цикл с младших разрядов 
            prod = x * d + carry # Умножаем цифру на d и добавляем перенос
            current_digit = prod % 10 # Текущая цифра результата 
            carry = prod // 10
            res_rev.append(current_digit)

        while carry > 0: # Обрабатываем оставшийся перенос
            res_rev.append(carry % 10) # Добавляем старшие разряды от перенос
            carry //= 10

        res = list(reversed(res_rev))

        return self.__class__(res)
