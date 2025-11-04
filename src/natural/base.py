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
        return ''.join(str(d) for d in reversed(self.digits))

    def __repr__(self) -> str:
        return f"Natural({self.digits})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Natural):
            return False
        return self.digits == other.digits

    def copy(self) -> 'Natural':
        return Natural(self.digits.copy())
