from src.integer import Integer
from src.natural import Natural
from src.rational import Rational
from src.polynomial import Polynomial


def test_mul_pq_p_basic():
    """Базовые тесты умножения полинома на рациональное число"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([1])), Natural([1])),   # 1 (x^0)
        Rational(Integer(0, Natural([3])), Natural([1])),   # 3x (x^1)
        Rational(Integer(0, Natural([2])), Natural([1]))    # 2x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 1/2
    multiplier = Rational(Integer(0, Natural([1])), Natural([2]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: x^2 + 3/2x + 1/2 (без сокращения: 2/2x^2 + 3/2x + 1/2)
    assert len(result.coefficients) == 3
    assert result.coefficients[0].numerator.absolute.digits == [1]  # 1/2 * 1 = 1/2
    assert result.coefficients[0].numerator.sign == 0
    assert result.coefficients[0].denominator.digits == [2]
    
    assert result.coefficients[1].numerator.absolute.digits == [3]  # 1/2 * 3 = 3/2
    assert result.coefficients[1].numerator.sign == 0
    assert result.coefficients[1].denominator.digits == [2]
    
    assert result.coefficients[2].numerator.absolute.digits == [2]  # 1/2 * 2 = 2/2 (несокращенная)
    assert result.coefficients[2].numerator.sign == 0
    assert result.coefficients[2].denominator.digits == [2]


def test_mul_pq_p_zero():
    """Тест умножения полинома на ноль"""
    # Полином: x^2 + 3x + 2 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),   # 2 (x^0)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 0
    multiplier = Rational(Integer(0, Natural([0])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Все коэффициенты должны стать нулями
    for coeff in result.coefficients:
        assert coeff.is_zero()


def test_mul_pq_p_negative():
    """Тест умножения полинома на отрицательное рациональное число"""
    # Полином: x^2 + 2x (коэффициенты от младшей степени к старшей)
    # Примечание: нулевой свободный член будет удален _validate()
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на -1/2
    multiplier = Rational(Integer(1, Natural([1])), Natural([2]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: -1/2x^2 - x (без сокращения: -2/2x - 1/2x^2)
    assert len(result.coefficients) == 2
    
    assert result.coefficients[0].numerator.absolute.digits == [2]  # 2 * (-1/2) = -2/2 (несокращенная)
    assert result.coefficients[0].numerator.sign == 1  # отрицательное
    assert result.coefficients[0].denominator.digits == [2]
    
    assert result.coefficients[1].numerator.absolute.digits == [1]  # 1 * (-1/2) = -1/2
    assert result.coefficients[1].numerator.sign == 1  # отрицательное
    assert result.coefficients[1].denominator.digits == [2]


def test_mul_pq_p_constant_polynomial():
    """Тест умножения константного полинома"""
    # Полином: 5 (константа)
    coeffs = [Rational(Integer(0, Natural([5])), Natural([1]))]
    poly = Polynomial(coeffs)
    
    # Умножаем на 3/4
    multiplier = Rational(Integer(0, Natural([3])), Natural([4]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: 15/4
    assert len(result.coefficients) == 1
    assert result.coefficients[0].numerator.absolute.digits == [1, 5]
    assert result.coefficients[0].numerator.sign == 0
    assert result.coefficients[0].denominator.digits == [4]


def test_mul_pq_p_identity():
    """Тест умножения на единицу (должно остаться без изменений)"""
    # Полином: x^2 + 3x + 2 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),   # 2 (x^0)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 1
    multiplier = Rational(Integer(0, Natural([1])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Результат должен быть равен исходному полиному
    assert len(result.coefficients) == len(poly.coefficients)
    for i in range(len(result.coefficients)):
        assert result.coefficients[i].numerator.absolute.digits == poly.coefficients[i].numerator.absolute.digits
        assert result.coefficients[i].numerator.sign == poly.coefficients[i].numerator.sign
        assert result.coefficients[i].denominator.digits == poly.coefficients[i].denominator.digits


def test_mul_pq_p_fractional_coefficients():
    """Тест умножения полинома с дробными коэффициентами"""
    # Полином: 1/4x^2 + 1/3x + 1/2 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([1])), Natural([2])),   # 1/2 (x^0)
        Rational(Integer(0, Natural([1])), Natural([3])),   # 1/3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([4]))    # 1/4x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 6
    multiplier = Rational(Integer(0, Natural([6])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: 3/2x^2 + 2x + 3 (без сокращения: 6/4x^2 + 6/3x + 6/2)
    assert len(result.coefficients) == 3
    assert result.coefficients[0].numerator.absolute.digits == [6]  # 1/2 * 6 = 6/2 (несокращенная)
    assert result.coefficients[0].denominator.digits == [2]
    
    assert result.coefficients[1].numerator.absolute.digits == [6]  # 1/3 * 6 = 6/3 (несокращенная)
    assert result.coefficients[1].denominator.digits == [3]
    
    assert result.coefficients[2].numerator.absolute.digits == [6]  # 1/4 * 6 = 6/4 (несокращенная)
    assert result.coefficients[2].denominator.digits == [4]


def test_mul_pq_p_immutability():
    """Тест, что исходный полином не изменяется"""
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),
        Rational(Integer(0, Natural([3])), Natural([1]))
    ]
    poly = Polynomial(coeffs)
    # Сохраняем исходные значения для проверки
    original_digits_0 = poly.coefficients[0].numerator.absolute.digits.copy()
    original_sign_0 = poly.coefficients[0].numerator.sign
    original_denom_0 = poly.coefficients[0].denominator.digits.copy()
    original_digits_1 = poly.coefficients[1].numerator.absolute.digits.copy()
    original_sign_1 = poly.coefficients[1].numerator.sign
    original_denom_1 = poly.coefficients[1].denominator.digits.copy()
    
    multiplier = Rational(Integer(0, Natural([2])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Исходный полином не должен измениться
    assert poly.coefficients[0].numerator.absolute.digits == original_digits_0
    assert poly.coefficients[0].numerator.sign == original_sign_0
    assert poly.coefficients[0].denominator.digits == original_denom_0
    assert poly.coefficients[1].numerator.absolute.digits == original_digits_1
    assert poly.coefficients[1].numerator.sign == original_sign_1
    assert poly.coefficients[1].denominator.digits == original_denom_1

