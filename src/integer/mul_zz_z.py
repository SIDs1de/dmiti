from .base_integer import BaseInteger


class Mul_zz_z:
    def mul_zz_z(self, second: BaseInteger) -> BaseInteger:
        """
        Приготовил: Viktor Permitin
        Умножение целых чисел
        """
        result = self.__class__(0, second.absolute.MUL_NN_N(self.absolute))
        if self.sign != second.sign:
            result = result.mul_zm_z()
        return result
        