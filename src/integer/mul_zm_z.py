from .base_integer import BaseInteger

class Mul_zm_z:
    def mul_zm_z(self: BaseInteger) -> BaseInteger:
        """
        Умножение целого числа на (-1)
        Возвращает новое число с противоположным знаком.
        Автор: Алиев Вусал гр. 4383
        """
        if self.is_zero():
            return BaseInteger(0, self.absolute)

        new_sign = -self.sign
        return BaseInteger(new_sign, self.absolute)
