from .base_integer import BaseInteger

class Div_zz_z:
    def div_zz_z(self: BaseInteger, other: BaseInteger) -> BaseInteger:
        """
        Нахождение частного от деления целого числа на целое
        Возвращает целое число со знаком
        Автор: Рубан Егор гр. 4383
        """
        if other.poz_z_d == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")

        module1 = self.abs_z_n()
        module2 = self.abs_z_n()

        q = module1.DIV_NN_N(module2)

        if (self.sign == other.sign):
            sign = 0
        else:
            sign = 1

        return BaseInteger(sign, q)
