from typing import Self

class Trans_n_z:
    def trans_n_z(self: Self):
        """
        Преобразование натурального числа в целое.
        Натуральное число всегда положительное,
        поэтому sign = 0.
        Автор: Алиев Вусал, гр. 4383
        """
        return self.__class__(0, self.absolute.copy())