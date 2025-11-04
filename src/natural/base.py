from typing import List

class Natural:
    """Базовый класс натурального числа"""

    def __init__(self, digits: List[int] = None) -> None:
        self.digits: List[int] = digits or [0]
        self._validate()

    def _validate(self) -> None:
        """Проверка корректности и удаление ведущих нулей"""
        if not self.digits:
            self.digits = [0]
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()

    def __str__(self) -> str:
        """Преобразование в строку для отображения числа"""
        return ''.join(str(d) for d in reversed(self.digits))

    def __repr__(self) -> str:
        """Технический вывод для отладки"""
        return f"Natural({self.digits})"

    def copy(self) -> 'Natural':
        "Создание независимой копии объекта"
        return Natural(self.digits.copy())
