from .base_integer import BaseInteger


class Add_zz_z:
    def add_zz_z(self, second: BaseInteger) -> BaseInteger:
        """
        Приготовил: Viktor Permitin
        Сложение целых чисел
        """
        first_sign = self.poz_z_d()
        second_sign = second.poz_z_d()
        if first_sign == 0:
            return self.__class__(second.sign, second.absolute.copy())
        if second_sign == 0:
            return self.__class__(self.sign, self.absolute.copy())
        is_sum = first_sign == second_sign
        result = None
        if is_sum:
            result = self.__class__(0, self.absolute.ADD_NN_N(second.absolute))
            if first_sign == 1:
                result = result.mul_zm_z()
        else:
            max_number, min_number = self.absolute, second.absolute
            max_number_sign = first_sign
            if max_number.COM_NN_D(min_number) == 1:
                max_number, min_number = min_number, max_number
                max_number_sign = second_sign
            result = self.__class__(0, max_number.SUB_NN_N(min_number))
            if max_number_sign == 1:
                result = result.mul_zm_z()
        return result
