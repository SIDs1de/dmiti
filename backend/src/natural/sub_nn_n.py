from typing import Self

class SUB_NN_N:
    def SUB_NN_N(self: Self, other: Self) -> Self:
        """
        Вычитание натуральных чисел
        Автор: Свинцов Егор гр. 4383
        Условие: self >= other
        Возвращает: натуральное число - разность self и other
        """
        # Проверяем, что self >= other
        comparison = self.COM_NN_D(other)
        if comparison == 1:
            raise ValueError("Первое число должно быть больше или равно второму")
        
        a_digits = self.digits.copy()  # Цифры уменьшаемого A = [aₙ, aₙ₋₁, ..., a₁, a₀]
        b_digits = other.digits        # Цифры вычитаемого B = [bₘ, bₘ₋₁, ..., b₁, b₀]
        
        # Выравниваем длины чисел, добавляя нули в начало более короткого числа
        max_len = max(len(a_digits), len(b_digits))
        a_digits = [0] * (max_len - len(a_digits)) + a_digits
        b_digits = [0] * (max_len - len(b_digits)) + b_digits
        
        result_digits = [0] * max_len  # Результирующие цифры C = [cₖ, cₖ₋₁, ..., c₁, c₀]
        borrow = 0  # Заём из старшего разряда (изначально borrow₀ = 0)
        
        # Вычитание с конца (младшие разряды)
        for i in range(max_len - 1, -1, -1):
            # Вычитаем с учётом заёма: aᵢ - bᵢ - borrowᵢ
            diff = a_digits[i] - b_digits[i] - borrow
            
            if diff < 0:
                # Если разность отрицательная, занимаем из старшего разряда
                diff += 10  # cᵢ = (aᵢ - bᵢ - borrowᵢ + 10) mod 10
                borrow = 1  # borrowᵢ₊₁ = 1
            else:
                borrow = 0  # borrowᵢ₊₁ = 0
                
            result_digits[i] = diff  # записывем результат
            
        return self.__class__(result_digits)  # Возвращаем новое натуральное число C = A - B