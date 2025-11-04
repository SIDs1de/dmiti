from .base_integer import Integer

class poz_z_d:
    """Z-2 Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
Предложили заменить на более стандартное обозначение и вывод как функции сигнум SGN_Z_D, где D равно -1, 0 или 1 соответственно"""

    def poz_z_d(self: Integer) -> int:
        if self.is_zero():
            return 0
        return 2 if self.sign > 0 else 1