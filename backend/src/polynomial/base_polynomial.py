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

    def is_zero(self) -> bool:
        """
        Проверка, является ли многочлен нулевым
        """
        for coeff in self.coefficients.values():
            if not coeff.is_zero():
                return False
        return True
    
    def __str__(self) -> str:
        """Преобразование в строку для отображения полинома"""
        string_coefficients = []
        for index, coefficient in sorted(self.coefficients.items(), reverse=True):
            # Пропускаем нулевые коэффициенты
            if coefficient.is_zero():
                continue
            
            # Проверяем, равен ли коэффициент 1/1 или -1/1
            is_one = (coefficient.numerator.sign == 0 and 
                     coefficient.numerator.absolute.digits == [1] and 
                     coefficient.denominator.digits == [1])
            is_minus_one = (coefficient.numerator.sign == 1 and 
                           coefficient.numerator.absolute.digits == [1] and 
                           coefficient.denominator.digits == [1])
            
            # Проверяем, отрицательный ли коэффициент
            is_negative = coefficient.numerator.sign == 1
            
            # Проверяем, равен ли знаменатель 1
            is_denominator_one = coefficient.denominator.digits == [1]
            
            if index == 0:
                # Для свободного члена показываем коэффициент
                if is_denominator_one:
                    # Если знаменатель 1, показываем только числитель
                    monomial = str(coefficient.numerator)
                else:
                    monomial = str(coefficient)
            elif is_one:
                # Если коэффициент 1/1, не показываем его
                if index == 1:
                    monomial = "x"
                else:
                    monomial = f"x^{index}"
            elif is_minus_one:
                # Если коэффициент -1/1, показываем только минус
                if index == 1:
                    monomial = "-x"
                else:
                    monomial = f"-x^{index}"
            else:
                # Для остальных случаев показываем коэффициент
                # Если коэффициент отрицательный, убираем знак минус (он будет добавлен позже)
                if is_denominator_one:
                    # Если знаменатель 1, показываем только числитель
                    coeff_str = str(coefficient.numerator)
                else:
                    coeff_str = str(coefficient)
                
                if is_negative and coeff_str.startswith("-"):
                    coeff_str = coeff_str[1:]  # Убираем минус
                
                if index == 1:
                    monomial = f"({coeff_str}) * x"
                else:
                    monomial = f"({coeff_str}) * x^{index}"
            
            string_coefficients.append((is_negative, monomial))
        
        if not string_coefficients:
            return "0"
        
        # Формируем строку с правильной обработкой знаков
        result_parts = []
        for i, (is_negative, monomial) in enumerate(string_coefficients):
            if i == 0:
                # Первый член: если отрицательный и monomial не начинается с минуса, добавляем минус
                if is_negative and not monomial.startswith("-"):
                    result_parts.append("-" + monomial)
                else:
                    result_parts.append(monomial)
            else:
                # Для остальных членов добавляем знак
                if is_negative:
                    # Убираем минус из monomial, если он там есть, и добавляем " - "
                    if monomial.startswith("-"):
                        result_parts.append(" - " + monomial[1:])
                    else:
                        result_parts.append(" - " + monomial)
                else:
                    result_parts.append(" + " + monomial)
        
        return ''.join(result_parts)

    def __repr__(self) -> str:
        """Технический вывод для отладки"""
        return f"Polynomial({str(self)})"

    def copy(self) -> 'Polynomial':
        """Создание независимой копии полинома"""
        return self.__class__(self.coefficients.copy())
