from typing import Self

class DIV_NN_DK:
    def DIV_NN_DK(self: Self, second: Self, k: int) -> int:
        """
        Автор: Viktor Permitin
        Вычисление первой цифры деления
        большего натурального на меньшее,
        домноженное на 10^k,где k - номер
        позиции этой цифры (номер считается
        с нуля)
        """
        # Проводит бинарный поиск и ищет подходящее число(максимально большой, но меньше чем делимое)
        # Проверка корректности степени k (должна быть неотрицательной)
        if k < 0:
            raise ValueError("k must be non-negative")
        
        # Проверка деления на ноль
        if len(second.digits) == 1 and second.digits[0] == 0:
            raise ValueError("division by zero")

        # Сдвигаем делитель влево на k позиций (умножаем на 10^k)
        # Это эквивалентно умножению делителя на 10^k
        shifted = second.MUL_Nk_N(k)

        # Если сдвинутый делитель больше делимого, первая цифра частного равна 0
        # cmp_result == 1 означает, что shifted > self
        if self.COM_NN_D(shifted) == 1:
            return 0

        # Бинарный поиск максимальной цифры d (0-9), такой что (shifted * d) <= self
        low, high = 0, 9  # Диапазон возможных цифр
        best = 0  # Найденная максимальная подходящая цифра
        
        while low <= high:
            mid = (low + high) // 2  # Средняя цифра для проверки
            candidate = shifted.MUL_ND_N(mid)  # shifted * mid
            
            # Сравниваем candidate с делимым
            # cmp: 2 - candidate < self, 0 - candidate == self, 1 - candidate > self
            cmp = self.COM_NN_D(candidate)
            
            if cmp == 2 or cmp == 0:
                # candidate <= self, значит mid - подходящая цифра
                # Пробуем увеличить mid для поиска максимальной подходящей цифры
                best = mid
                low = mid + 1
            else:
                # candidate > self, значит mid слишком большая
                # Уменьшаем диапазон поиска
                high = mid - 1
        
        # Возвращаем найденную максимальную цифру
        return best
