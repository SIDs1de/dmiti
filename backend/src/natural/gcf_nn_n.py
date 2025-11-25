from .enums import BoolResult
from typing import Self

class GCF_NN_N:
    def GCF_NN_N(self: Self, other: Self) -> Self:
        """
        Метод нахождения НОД двух натуральных чисел.
        Результат - натуральное число.
        Автор: Рубан Егор гр. 4383
        """

        # Если второе число больше первого, меняем их местами
        # COM_NN_D возвращает:
        # 1 — если self < other
        if self.COM_NN_D(other) == 1:
            self, other = other, self

        # Основной цикл алгоритма Евклида
        # Продолжаем выполнять деление с остатком, пока второе число не станет нулём
        # NZER_N_B возвращает BoolResult.YES, если число не равно нулю
        while other.NZER_N_B() == BoolResult.YES:

            # Сравниваем текущее self и other
            comp = self.COM_NN_D(other)

            if comp == 0:
                # Если числа равны — это и есть НОД
                return self
            elif comp == 1:
                # Если self < other, меняем их местами
                self, other = other, self

            # Находим остаток от деления self на other
            R = self.MOD_NN_N(other)
            # Переходим к следующей итерации алгоритма Евклида:
            # (a, b) → (b, a mod b)
            self, other = other, R

        # Когда other стал нулём, self содержит НОД
        return self


