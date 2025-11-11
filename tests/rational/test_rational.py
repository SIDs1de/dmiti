from src.integer import Integer
from src.natural import Natural
from src.rational import Rational


def test_mul_qq_q_basic():
    """Базовые тесты умножения дробей"""
    a = Rational(Integer(0, Natural([1])), Natural([2]))
    b = Rational(Integer(0, Natural([3])), Natural([4]))
    result = a.MUL_QQ_Q(b)
    assert result.numerator.absolute.digits == [3]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [8]

def test_mul_qq_q_zero():
    """Тесты умножения на ноль"""
    a = Rational(Integer(0, Natural([0])), Natural([1]))
    b = Rational(Integer(0, Natural([1])), Natural([2]))
    result = a.MUL_QQ_Q(b)
    assert result.numerator.absolute.digits == [0]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [2]

def test_mul_qq_q_negative():
    """Тесты умножения на отрицательную дробь"""
    a = Rational(Integer(0, Natural([2])), Natural([3]))
    b = Rational(Integer(1, Natural([3])), Natural([4]))
    result = a.MUL_QQ_Q(b)
    assert result.numerator.absolute.digits == [6]
    assert result.numerator.sign == 1
    assert result.denominator.digits == [1, 2]

def test_mul_qq_both_negative():
    """Проверка умножения отрицательных дробей"""
    a = Rational(Integer(1, Natural([1])), Natural([1]))
    b = Rational(Integer(1, Natural([1])), Natural([2]))
    result = a.MUL_QQ_Q(b)
    assert result.numerator.absolute.digits == [1]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [2]

def test_int_q_b_zero():
    """Тест с нулевым числителем - должно быть целым"""
    rational = Rational(Integer(0, Natural([0])), Natural([5]))
    result = rational.INT_Q_B()
    assert result == "да"

def test_int_q_b_positive_integer():
    """Тест с положительным целым (знаменатель = 1)"""
    rational = Rational(Integer(0, Natural([5])), Natural([1]))
    result = rational.INT_Q_B()
    assert result == "да"

def test_int_q_b_negative_integer():
    """Тест с отрицательным целым (знаменатель = 1)"""
    rational = Rational(Integer(1, Natural([7])), Natural([1]))
    result = rational.INT_Q_B()
    assert result == "да"

def test_int_q_b_positive_fraction():
    """Тест с положительной дробью (не целое)"""
    rational = Rational(Integer(0, Natural([3])), Natural([2]))
    result = rational.INT_Q_B()
    assert result == "нет"

def test_int_q_b_negative_fraction():
    """Тест с отрицательной дробью (не целое)"""
    rational = Rational(Integer(1, Natural([5])), Natural([3]))
    result = rational.INT_Q_B()
    assert result == "нет"

def test_int_q_b_large_integer():
    """Тест с большим целым числом"""
    rational = Rational(Integer(0, Natural([1, 2, 3])), Natural([1]))
    result = rational.INT_Q_B()
    assert result == "да"

def test_int_q_b_large_fraction():
    """Тест с большой дробью (не целое)"""
    rational = Rational(Integer(0, Natural([1, 0, 0])), Natural([9, 9]))
    result = rational.INT_Q_B()
    assert result == "нет"