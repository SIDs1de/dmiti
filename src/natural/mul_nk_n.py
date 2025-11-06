from .base import BaseNatural

class MUL_Nk_N:
    def MUL_Nk_N(self: BaseNatural, k: int) -> BaseNatural:
        """
        Умножение натурального числа на 10^k.
        Автор: Карпов Андрей гр. 4382
        Возвращает новый объект того же класса.
        """
        # Проверки типа и диапазона
        if not isinstance(k, int):
            raise TypeError("k must be int")
        if k < 0:
            raise ValueError("k must be non-negative")

        # Быстрые случаи
        if k == 0:
            return self.copy()
        if len(self.digits) == 1 and self.digits[0] == 0:
            return self.__class__([0])

        # Основная операция: добавляем k нулей к списку digits
        new_digits = self.digits.copy() + [0] * k
        return self.__class__(new_digits)
