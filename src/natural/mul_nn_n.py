from .base import BaseNatural

class MUL_NN_N:
    def MUL_NN_N(self: BaseNatural, other: BaseNatural) -> BaseNatural:
        """
        Умножение двух натуральных чисел.
        Автор: Карпов Андрей гр. 4382
        Возвращает новый объект того же класса.
        """
        # Проверка входного аргумента
        if not hasattr(other, 'digits'):
            raise TypeError("other must be a natural number")

        # Быстрые случаи
        if len(self.digits) == 1 and self.digits[0] == 0:
            return self.__class__([0])
        if len(other.digits) == 1 and other.digits[0] == 0:
            return self.__class__([0])

        result = self.__class__([0]) 
        shift = 0 # количество добавляемых нулей

        # Основной алгоритм: проходим по цифрам второго множителя справа налево
        for d in reversed(other.digits):
            if d == 0:
                partial = self.__class__([0])
            else:
                partial = self.MUL_ND_N(d)
            if shift > 0:
                partial = partial.MUL_Nk_N(shift)
            result = result.ADD_NN_N(partial)
            shift += 1

        return result