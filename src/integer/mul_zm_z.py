from .base_integer import BaseInteger

class Mul_zm_z:
    def mul_zm_z(self):
        """
        Умножение целого числа на (-1)
        Возвращает новое число с противоположным знаком.
        Автор: Алиев Вусал гр. 4383
        """
        if self.is_zero():
            return self.__class__(0, self.absolute)

        return self.__class__(0 if self.sign == 1 else 1, self.absolute)