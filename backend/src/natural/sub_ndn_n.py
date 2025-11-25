from typing import Self

class SUB_NDN_N:
    def SUB_NDN_N(self: Self, second: Self, d: int) -> Self:
        """
        Автор: Viktor Permitin
        Вычитание из натурального другого
        натурального, умноженного на цифру
        """
        # Домножается число на циифру -> вычитается
        # Проверка корректности цифры d (должна быть от 0 до 9)
        if d < 0 or d > 9:
            raise ValueError("d must be in 0..9 (digit)")
        
        # Умножаем вычитаемое на цифру d
        second = second.MUL_ND_N(d)
        
        # Сравниваем результат умножения с уменьшаемым
        # cmp_result: 2 - если second > self, 0 - если равны, 1 - если second < self
        cmp_result = second.COM_NN_D(self)
        
        # Если результат умножения больше уменьшаемого, результат будет отрицательным
        # Это недопустимо для натуральных чисел, поэтому выбрасываем исключение
        if cmp_result >= 2:
            raise ValueError("Result must be positive (macan)")
        
        # Выполняем вычитание: self - (second * d)
        return self.SUB_NN_N(second)
