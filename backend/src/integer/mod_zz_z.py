from typing import Self

class MOD_ZZ_Z:
    def MOD_ZZ_Z(self: Self, other: Self) -> Self:
        """
        Остаток от деления целого на целое (делитель отличен от нуля)
        Автор: Свинцов Егор гр. 4383
        
        Математическая формула: 
        Для целых чисел a и b (b ≠ 0) находим r = a mod b такой, что:
        a = b × q + r, где 0 ≤ r < |b|
        """
        if other.poz_z_d() == 0:  # Проверка: b ≠ 0
            raise ZeroDivisionError("Деление на ноль невозможно")
        
        # Вычисление частного q = ⌊a/b⌋ (целочисленное деление)
        quotient = self.div_zz_z(other)
        
        # Вычисление остатка: r = a - b × q
        remainder = self.sub_zz_z(other.mul_zz_z(quotient))
        
        # Корректировка знака: если r < 0, то r = r + |b|
        # Это обеспечивает выполнение условия 0 ≤ r < |b|
        if remainder.sign == 1 and not remainder.is_zero():
            remainder = remainder.add_zz_z((other.abs_z_n()).trans_n_z())
        
        # Возвращаем остаток r, удовлетворяющий условию 0 ≤ r < |b|
        return remainder