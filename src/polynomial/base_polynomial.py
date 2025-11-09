from typing import List, Optional
from src.rational import Rational
from src.integer import Integer
from src.natural import Natural


class BasePolynomial:
    """Базированный класс для полиномов"""

    def __init__(self, coefficients: Optional[List[Rational]] = None) -> None:
        self.coefficients = coefficients or [Rational(Integer(0, Natural([0])), Natural([1]))]
        self._validate()

    @property
    def m(self):
        return len(self.coefficients) - 1

    def _validate(self) -> None:
        """Проверка корректности и удаление ведущих нулей"""
        while len(self.coefficients) > 1 and self.coefficients[0].is_zero():
            self.coefficients.pop(0)
        if not self.coefficients:
            self.coefficients = [Rational(Integer(0, Natural([0])), Natural([1]))]
    
    def __str__(self) -> str:
        """Преобразование в строку для отображения полинома"""
        string_coefficients = []
        for index, coefficient in enumerate(self.coefficients):
            monomial = f"({coefficient.str()})"
            if index != len(self.coefficients) - 1:
                monomial += f" * x^{len(self.coefficients) - index - 1}"
            string_coefficients.append(monomial)
        return ' + '.join(string_coefficients)

    def __repr__(self) -> str:
        """Технический вывод для отладки"""
        return f"Polynomial({str(self)})"

    def copy(self) -> 'Polynomial':
        """Создание независимой копии полинома"""
        return self.__class__(self.coefficients.copy())
