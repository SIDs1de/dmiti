from .base import Natural


class NaturalArithmetic:
    """Базовые арифметические методы"""

    def add_1n_n(self: Natural) -> Natural:
        """N-3: Добавление 1 к натуральному числу"""
        result = self.copy()
        carry = 1

        for i in range(len(result.digits)):
            result.digits[i] += carry
            carry = result.digits[i] // 10
            result.digits[i] %= 10
            if carry == 0:
                break

        if carry > 0:
            result.digits.append(carry)

        return result

    def add_nn_n(self: Natural, other: Natural) -> Natural:
        """N-4: Сложение натуральных чисел"""
        # TODO: Реализовать
        return Natural([0])

    def sub_nn_n(self: Natural, other: Natural) -> Natural:
        """N-5: Вычитание (self >= other)"""
        # TODO: Реализовать
        return Natural([0])
