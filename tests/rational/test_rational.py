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

def test_add_positive_fractions():
    """Сложение двух положительных дробей"""
    num1 = Integer(0, Natural([1]))
    den1 = Natural([2])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([1]))
    den2 = Natural([3])
    frac2 = Rational(num2, den2)
    
    result = frac1.ADD_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([5]))
    expected_den = Natural([6])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits
    
def test_add_negative_fractions():
    """Сложение двух отрицательных дробей"""
    num1 = Integer(1, Natural([1]))
    den1 = Natural([4])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(1, Natural([1]))
    den2 = Natural([4])
    frac2 = Rational(num2, den2)
    
    result = frac1.ADD_QQ_Q(frac2)
    
    expected_num = Integer(1, Natural([2]))  
    expected_den = Natural([4])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_add_mixed_sign_fractions():
    """Сложение дробей с разными знаками"""
    num1 = Integer(0, Natural([3]))
    den1 = Natural([4])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(1, Natural([1]))
    den2 = Natural([4])
    frac2 = Rational(num2, den2)
    
    result = frac1.ADD_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([2]))  
    expected_den = Natural([4])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_add_with_zero():
    """Сложение с нулевой дробью"""
    num1 = Integer(0, Natural([2]))
    den1 = Natural([3])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([0]))
    den2 = Natural([1])
    frac2 = Rational(num2, den2)
    
    result = frac1.ADD_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([2]))
    expected_den = Natural([3])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_add_zero_with_zero():
    """Сложение двух нулевых дробей"""
    num1 = Integer(0, Natural([0]))
    den1 = Natural([1])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([0]))
    den2 = Natural([1])
    frac2 = Rational(num2, den2)
    
    result = frac1.ADD_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([0]))
    expected_den = Natural([1])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_add_large_numbers():
    """Сложение дробей с большими числами"""
    num1 = Integer(0, Natural([1, 2, 3]))
    den1 = Natural([4, 5, 6])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([7, 8, 9]))
    den2 = Natural([1, 0, 0, 0])
    frac2 = Rational(num2, den2)
    
    result = frac1.ADD_QQ_Q(frac2)
    
    assert result.numerator.sign == 0
    assert len(result.numerator.absolute.digits) > 0
    assert len(result.denominator.digits) > 0

def test_rational_initialization_zero_denominator():
    """Проверка исключения при создании дроби с нулевым знаменателем"""
    num = Integer(0, Natural([1]))
    den = Natural([0])
    
    try:
        frac = Rational(num, den)
        assert False, "Должно было возникнуть исключение ZeroDivisionError"
    except ZeroDivisionError:
        assert True
    except Exception:
        assert False, "Возникло неправильное исключение"


def test_red_q_q_basic():
    """Базовые тесты сокращения дроби"""
    # Дробь: 4/6 должна сократиться до 2/3
    fraction = Rational(Integer(0, Natural([4])), Natural([6]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [2]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [3]


def test_red_q_q_already_reduced():
    """Тест сокращения уже сокращенной дроби"""
    # Дробь: 2/3 уже сокращена
    fraction = Rational(Integer(0, Natural([2])), Natural([3]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [2]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [3]


def test_red_q_q_negative():
    """Тест сокращения отрицательной дроби"""
    # Дробь: -6/8 должна сократиться до -3/4
    fraction = Rational(Integer(1, Natural([6])), Natural([8]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [3]
    assert result.numerator.sign == 1  # отрицательное
    assert result.denominator.digits == [4]


def test_red_q_q_zero_numerator():
    """Тест сокращения дроби с нулевым числителем"""
    # Дробь: 0/5 должна стать 0/1
    fraction = Rational(Integer(0, Natural([0])), Natural([5]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [0]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [1]


def test_red_q_q_large_numbers():
    """Тест сокращения дроби с большими числами"""
    # Дробь: 24/36 должна сократиться до 2/3
    fraction = Rational(Integer(0, Natural([2, 4])), Natural([3, 6]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [2]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [3]


def test_red_q_q_prime_numbers():
    """Тест сокращения дроби с простыми числами"""
    # Дробь: 7/11 (простые числа) не должна сокращаться
    fraction = Rational(Integer(0, Natural([7])), Natural([1, 1]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [7]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [1, 1]


def test_red_q_q_common_factor():
    """Тест сокращения дроби с общим множителем"""
    # Дробь: 15/25 должна сократиться до 3/5
    fraction = Rational(Integer(0, Natural([1, 5])), Natural([2, 5]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [3]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [5]


def test_red_q_q_negative_denominator():
    """Тест что знаменатель всегда остается натуральным (положительным)"""
    # Дробь: -4/6 должна стать -2/3 (знаменатель положительный)
    fraction = Rational(Integer(1, Natural([4])), Natural([6]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [2]
    assert result.numerator.sign == 1  # отрицательное
    assert result.denominator.digits == [3]  # положительное


def test_red_q_q_immutability():
    """Тест, что исходная дробь не изменяется"""
    fraction = Rational(Integer(0, Natural([4])), Natural([6]))

    # Сохраняем исходные значения
    original_num_digits = fraction.numerator.absolute.digits.copy()
    original_num_sign = fraction.numerator.sign
    original_denom_digits = fraction.denominator.digits.copy()

    result = fraction.RED_Q_Q()

    # Исходная дробь не должна измениться
    assert fraction.numerator.absolute.digits == original_num_digits
    assert fraction.numerator.sign == original_num_sign
    assert fraction.denominator.digits == original_denom_digits

    # Проверяем, что результат корректен
    assert result.numerator.absolute.digits == [2]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [3]


def test_red_q_q_complex_case():
    """Тест сложного случая сокращения"""
    # Дробь: 100/250 должна сократиться до 2/5
    fraction = Rational(Integer(0, Natural([1, 0, 0])), Natural([2, 5, 0]))
    result = fraction.RED_Q_Q()

    assert result.numerator.absolute.digits == [2]
    assert result.numerator.sign == 0
    assert result.denominator.digits == [5]