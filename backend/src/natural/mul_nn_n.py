from typing import Self

class MUL_NN_N:
    def MUL_NN_N(self: Self, other: Self) -> Self:
        """
        Умножение двух натуральных чисел.
        Автор: Карпов Андрей гр. 4382
        Возвращает новый объект того же класса.
        """
        # Проверка входного аргумента
        if not hasattr(other, 'digits'):
            raise TypeError("other must be a natural number")

        # Быстрые случаи
        if len(self.digits) == 1 and self.digits[0] == 0: # Если первое число равно 0, результат — 0
            return self.__class__([0])
        if len(other.digits) == 1 and other.digits[0] == 0: # Если второе число равно 0, результат — 0

            return self.__class__([0])

        result = self.__class__([0]) 
        shift = 0 # количество добавляемых нулей

        # Основной алгоритм: проходим по цифрам второго множителя справа налево
        for d in reversed(other.digits):
            if d == 0:
                partial = self.__class__([0]) # Если цифра второго числа равна 0, пропускаем её
            else:
                partial = self.MUL_ND_N(d) # Умножаем первое число на текущую цифру второго числа (поочередно)
            if shift > 0:
                partial = partial.MUL_Nk_N(shift) # Добавляем нули
            result = result.ADD_NN_N(partial) # Добавляем частичное произведение к результату
            shift += 1 # Увеличиваем сдвиг на 1, чтобы добавить еще один ноль для следующей цифры

        return result