from .base import Natural

class COM_NN_D:
    def COM_NN_D(self: Natural, other: Natural) -> int:
        """
        Сравнение натуральных чисел
        Автор: Свинцов Егор гр. 4383
        """
        # Сравниваем количество цифр (длину числа)
        if len(self.digits) > len(other.digits):
            return 2
        elif len(self.digits) < len(other.digits):
            return 1
        
        # Если длины равны, то сравниваем по цифрам
        for i in range(len(self.digits) - 1, -1, -1):
            if self.digits[i] > other.digits[i]:
                return 2
            elif self.digits[i] < other.digits[i]:
                return 1
            
        # Все цифры равны
        return 0