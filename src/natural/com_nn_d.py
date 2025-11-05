from .base import Natural

class COM_NN_D:
    def COM_NN_D(self: Natural, other: Natural) -> int:
        """
        Сравнение натуральных чисел
        Автор: Свинцов Егор гр. 4383
        Возвращает:
        2 - если первое больше второго
        0 - если равны
        1 - иначе
        """
        # Сравниваем количество цифр (длину числа)
        if len(self.digits) > len(other.digits):
            return 2
        elif len(self.digits) < len(other.digits):
            return 1
        
        # Если длины равны, то сравниваем по цифрам
        for i in range(len(self.digits)):
            if self.digits[i] > other.digits[i]:
                return 2
            elif self.digits[i] < other.digits[i]:
                return 1
            
        # Все цифры равны
        return 0