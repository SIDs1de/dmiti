from typing import Self

class GCF_PP_P:
    def GCF_PP_P(self: Self, other: Self) -> Self:
        """
        НОД двух многочленов методом Евклида.
        Автор: Карпов Андрей, гр. 4382
        Возвращает многочлен - НОД двух многочленов.
        """
        a = self.copy()
        b = other.copy()

        # Алгоритм Евклида: gcd(a, b) = gcd(b, a mod b), пока b ≠ 0
        while not b.is_zero():
            r = a.MOD_PP_P(b)  # Находим остаток от деления a на b
            a = b
            b = r

        return a # Возвращаем НОД, который будет в a после завершения цикла