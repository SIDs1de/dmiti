from typing import Self

class Add_zz_z:
    def add_zz_z(self: Self, second: Self) -> Self:
        """
        Приготовил: Viktor Permitin
        Сложение целых чисе
        """
        # Складывает числа 2 случая
        # Определяем знаки обоих чисел
        first_sign = self.poz_z_d()
        second_sign = second.poz_z_d()
        
        # Если первое слагаемое равно нулю, возвращаем второе
        if first_sign == 0:
            return self.__class__(second.sign, second.absolute.copy())
        
        # Если второе слагаемое равно нулю, возвращаем первое
        if second_sign == 0:
            return self.__class__(self.sign, self.absolute.copy())
        
        # Проверяем, одинаковые ли знаки у слагаемых
        is_sum = first_sign == second_sign
        result = None
        
        if is_sum:
            # Случай 1: Оба числа одного знака (оба положительные или оба отрицательные)
            # Складываем абсолютные значения
            result = self.__class__(0, self.absolute.ADD_NN_N(second.absolute))
            
            # Если оба числа отрицательные, результат тоже отрицательный
            if first_sign == 1:
                result = result.mul_zm_z()  # Умножаем на -1
        else:
            # Случай 2: Числа разных знаков (одно положительное, другое отрицательное)
            # Находим большее и меньшее по модулю
            max_number, min_number = self.absolute, second.absolute
            max_number_sign = first_sign  # Знак большего по модулю числа
            
            # Если второе число по модулю больше первого, меняем их местами
            if max_number.COM_NN_D(min_number) == 1:
                max_number, min_number = min_number, max_number
                max_number_sign = second_sign
            
            # Вычитаем меньшее из большего (по модулю)
            result = self.__class__(0, max_number.SUB_NN_N(min_number))
            
            # Присваиваем знак большего по модулю числа
            if max_number_sign == 1:
                result = result.mul_zm_z()  # Умножаем на -1
        
        return result
