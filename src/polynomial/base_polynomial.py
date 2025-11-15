from typing import Dict, Optional
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural


class BasePolynomial:
    """Базированный класс для полиномов"""

    def __init__(self, coefficients: Optional[Dict[int, Rational]] = None) -> None:
        self.coefficients = coefficients or {0: Rational(Integer(0, Natural([0])), Natural([1]))}
        self.m = max(self.coefficients.keys())
        self._validate()

    def _validate(self) -> None:
        """Проверка корректности и удаление ведущих нулей"""
        while self.m in self.coefficients and self.coefficients[self.m].is_zero():
            self.coefficients.pop(self.m)
            self.m = max(self.coefficients.keys() or [0])
        if not self.coefficients:
            self.coefficients = {0: Rational(Integer(0, Natural([0])), Natural([1]))}
    
    def __str__(self) -> str:
        """Преобразование в строку для отображения полинома"""
        string_coefficients = []
        for index, coefficient in self.coefficients.items():
            monomial = f"({str(coefficient)})"
            if index != 0:
                monomial += f" * x^{index}"
            string_coefficients.append(monomial)
        return ' + '.join(string_coefficients)

    def __repr__(self) -> str:
        """Технический вывод для отладки"""
        return f"Polynomial({str(self)})"

    def copy(self) -> 'Polynomial':
        """Создание независимой копии полинома"""
        return self.__class__(self.coefficients.copy())
