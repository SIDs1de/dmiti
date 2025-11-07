from .base import BaseNatural

class ADD_NN_N:
    def ADD_NN_N(self: BaseNatural, other: BaseNatural) -> BaseNatural:
        """
        Сложение натуральных чисел
        Автор: Свинцов Егор гр. 4383
        Возвращает: новое натуральное число - сумму self и other
        """
        a_digits = self.digits
        b_digits = other.digits
        
        # Определяем максимальную длину
        max_len = max(len(a_digits), len(b_digits))
        result_digits = [0] * max_len
        carry = 0 # Перенос
        
        # Сложение с конца (младшие разряды)
        for i in range(1, max_len + 1):
            digit_a = a_digits[-i] if i <= len(a_digits) else 0
            digit_b = b_digits[-i] if i <= len(b_digits) else 0
            total = digit_a + digit_b + carry
            carry = total // 10
            result_digits[-i] = total % 10
            
        # Если остался перенос, добавляем новый разряд
        if carry > 0:
            result_digits.insert(0, carry)
            
        return self.__class__(result_digits)