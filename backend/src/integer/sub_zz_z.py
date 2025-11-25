from typing import Self

class Sub_zz_z:
    def sub_zz_z(self: Self, second: Self) -> Self:
        """
        Приготовил: Viktor Permitin
        Вычитание целых чисел
        """
        # Вычитание реализуется как сложение с противоположным числом
        # self - second = self + (-second)
        # mul_zm_z() умножает число на -1 (меняет знак)
        return self.add_zz_z(second.mul_zm_z())
