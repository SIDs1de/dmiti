from typing import Self

class DIV_NN_N:
    def DIV_NN_N(self: Self, second: Self) -> Self:
        """
        Автор: Viktor Permitin
        Неполное частное от деления первого
        натурального числа на второе с
        остатком (делитель отличен от нуля)
        """
        # Максимальное кол-во разрядов -> для каждого разряда вычисляется цифра в частном и вычитается домноженная на степень 10
        # Проверка деления на ноль
        if len(second.digits) == 1 and second.digits[0] == 0:
            raise ValueError("division by zero")
    
        # Сравниваем делимое и делитель
        # cmp_result: 2 - self > second, 0 - self == second, 1 - self < second
        cmp_result = self.COM_NN_D(second)
        
        # Если делимое меньше делителя, частное равно 0
        if cmp_result == 1:
            return self.__class__([0])
        
        # Если делимое равно делителю, частное равно 1
        if cmp_result == 0:
            return self.__class__([1])
        
        # Определяем максимальную степень для начала деления
        # k_max - это разница в количестве разрядов между делимым и делителем
        # Это позволяет начать деление с правильной позиции
        # Также k_max позволяет определить максимальное количество цифр
        # в результирующем частном.
        k_max = len(self.digits) - len(second.digits)
        
        # Копируем делимое - это будет остаток, который мы будем уменьшать
        remainder = self.copy()
        result_digits = []  # Массив цифр результата (частного)
        
        # Проходим по всем позициям от старшей (k_max) до младшей (0)
        # Это соответствует алгоритму деления "в столбик" слева направо
        for k in range(k_max, -1, -1):
            # Находим цифру частного на позиции k
            # DIV_NN_DK находит максимальную цифру d, такую что
            # (second * 10^k * d) <= remainder
            digit = remainder.DIV_NN_DK(second, k)
            
            # Если найденная цифра > 0, вычитаем соответствующее произведение из остатка
            if digit > 0:
                # Сдвигаем делитель влево на k позиций (умножаем на 10^k)
                shifted = second.MUL_Nk_N(k)
                # Умножаем сдвинутый делитель на найденную цифру
                product = shifted.MUL_ND_N(digit)
                # Вычитаем произведение из остатка
                remainder = remainder.SUB_NN_N(product)
            
            # Пропускаем ведущие нули (не добавляем их в начало результата)
            if len(result_digits) == 0 and digit == 0:
                continue
            
            # Добавляем найденную цифру в результат
            result_digits.append(digit)
        
        # Удаляем ведущие нули из результата (если они остались)
        # Это может произойти, если все цифры на старших позициях были нулями
        while len(result_digits) > 1 and result_digits[0] == 0:
            result_digits.pop(0)
        
        # Возвращаем частное как новое натуральное число
        return self.__class__(result_digits)