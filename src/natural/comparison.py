from .base import Natural


class NaturalComparison:
    """Методы сравнения натуральных чисел"""

    def com_nn_d(self: Natural, other: Natural) -> int:
        """
        N-1: Сравнение натуральных чисел
        Возвращает: 2 если self > other, 0 если равно, 1 если self < other
        """
        if len(self.digits) > len(other.digits):
            return 2
        elif len(self.digits) < len(other.digits):
            return 1

        for i in range(len(self.digits) - 1, -1, -1):
            if self.digits[i] > other.digits[i]:
                return 2
            elif self.digits[i] < other.digits[i]:
                return 1

        return 0

    def nzer_n_b(self: Natural) -> str:
        """
        N-2: Проверка на ноль
        Возвращает "да" если число не равно нулю, иначе "нет"
        """
        return "да" if not (len(self.digits) == 1 and self.digits[0] == 0) else "нет"
