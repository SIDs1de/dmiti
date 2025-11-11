from src.natural import Natural
from src.integer import Integer


class BaseRational:
    """Класс рациональных чисел (дробей) — пара (целое; натуральное)"""

    def __init__(self, numerator: Integer, denominator: Natural):
        if denominator.digits == [0]:
            raise ZeroDivisionError("Знаменатель не может быть нулём")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Rational({self.numerator!r}, {self.denominator!r})"

    def is_zero(self):
        """Проверяет, что дробь равна нулю"""
        return self.numerator.is_zero()