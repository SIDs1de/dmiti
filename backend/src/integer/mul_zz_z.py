from typing import Self

class Mul_zz_z:
    def mul_zz_z(self: Self, second: Self) -> Self:
        """
        Приготовил: Viktor Permitin
        Умножение целых чисел
        """
        # Умножаем абсолютные значения обоих чисел
        # Результат изначально положительный (sign = 0)
        result = self.__class__(0, second.absolute.MUL_NN_N(self.absolute))
        
        # Применяем правило знаков:
        # Если знаки множителей разные, результат отрицательный
        # sign: 0 - положительное, 1 - отрицательное
        if self.sign != second.sign:
            result = result.mul_zm_z()  # Умножаем на -1 (меняем знак)
        
        return result
        