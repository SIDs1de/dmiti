from .base_integer import BaseInteger

class Poz_z_d:
    def poz_z_d(self: BaseInteger) -> int:
        """
        Определяет знак числа: 2-положительное, 0-ноль, 1-отрицательное
        Автор: Королев Семен гр. 4382
        """
        if self.is_zero():
            return 0
        return 2 if self.sign > 0 else 1