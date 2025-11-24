from typing import Self

class ADD_NN_N:
    def ADD_NN_N(self: Self, other: Self) -> Self:
        """
        Сложение натуральных чисел
        Автор: Свинцов Егор гр. 4383
        Возвращает: новое натуральное число - сумму self и other
        """
        a_digits = self.digits  # Цифры первого числа: A = [aₙ, aₙ₋₁, ..., a₁, a₀]
        b_digits = other.digits  # Цифры второго числа: B = [bₘ, bₘ₋₁, ..., b₁, b₀]
        
        # Определяем максимальную длину: max(n, m) + 1 (для возможного переноса)
        max_len = max(len(a_digits), len(b_digits))
        result_digits = [0] * max_len  # Результирующие цифры: S = [sₖ, sₖ₋₁, ..., s₁, s₀]
        carry = 0  # Перенос cᵢ (изначально c₀ = 0)
        
        # Сложение с конца (младшие разряды): для i от 0 до max(n,m)-1
        for i in range(1, max_len + 1):
            digit_a = a_digits[-i] if i <= len(a_digits) else 0  # aᵢ (если существует, иначе 0)
            digit_b = b_digits[-i] if i <= len(b_digits) else 0  # bᵢ (если существует, иначе 0)
            total = digit_a + digit_b + carry  # Временная сумма: temp = aᵢ + bᵢ + cᵢ
            carry = total // 10  # Новый перенос: cᵢ₊₁ = ⌊temp/10⌋
            result_digits[-i] = total % 10  # Текущий разряд результата: sᵢ = temp mod 10
            
        # Если остался перенос, добавляем новый разряд: sₖ = cₖ где k = max(n,m)
        if carry > 0:
            result_digits.insert(0, carry)  # Добавляем старший разряд: S = [cₖ, sₖ₋₁, ..., s₀]
            
        return self.__class__(result_digits)  # Возвращаем новое натуральное число S = A + B