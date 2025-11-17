from typing import Self

class MOD_ZZ_Z:
    def MOD_ZZ_Z(self: Self, other: Self) -> Self:
        """
        Остаток от деления целого на целое (делитель отличен от нуля)
        Автор: Свинцов Егор гр. 4383
        """
        if other.poz_z_d() == 0: # Проверка деления на ноль
            raise ZeroDivisionError("Деление на ноль невозможно")
        
        # Вычисление частного
        quotient = self.div_zz_z(other)
        
        # Вычисляем остаток
        remainder = self.sub_zz_z(other.mul_zz_z(quotient))
        
        if remainder.sign == 1 and not remainder.is_zero():
            remainder = remainder.add_zz_z((other.abs_z_n()).trans_n_z())
        
        return remainder
