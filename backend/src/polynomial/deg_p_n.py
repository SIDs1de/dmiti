from typing import Self
from src.natural import Natural


class DEG_P_N:
    def DEG_P_N(self: Self) -> Natural:
        """
        Возвращает степень многочлена
        Автор: Королев Семен гр. 4382
        """
        # Базовое назначение: возвращает степень многочлена из поля m, конвертируя в Natural

        degree = self.m  # Получаем целочисленную степень из объекта

        if degree == 0:
            return Natural([0])  # Нулевая степень - специальный случай

        digits = []
        temp = degree
        # Конвертация числа в цифры
        while temp > 0:
            digits.insert(0, temp % 10)  # Добавление цифры в начало
            temp //= 10  # Удаление обработанного разряда

        return Natural(digits)  # Создание Natural из цифр