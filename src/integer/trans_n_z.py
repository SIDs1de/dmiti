from src.natural import Natural
from .base_integer import BaseInteger

class Trans_n_z:
    def trans_n_z(self):
        """
        Преобразование натурального числа в целое.
        Натуральное число всегда положительное,
        поэтому sign = 0.
        Автор: Алиев Вусал, гр. 4383
        """
        return self.__class__(0, self.absolute.copy())