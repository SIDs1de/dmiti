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
        
def test_sub_positive_fractions():
    """Вычитание двух положительных дробей"""
    num1 = Integer(0, Natural([3]))
    den1 = Natural([4])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([1]))
    den2 = Natural([4])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([2])) 
    expected_den = Natural([4])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_sub_negative_fractions():
    """Вычитание отрицательных дробей"""
    num1 = Integer(1, Natural([1]))
    den1 = Natural([4])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(1, Natural([1]))
    den2 = Natural([4])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([0])) 
    expected_den = Natural([4])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_sub_mixed_sign_fractions():
    """Вычитание дробей с разными знаками"""
    num1 = Integer(0, Natural([3]))
    den1 = Natural([4])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(1, Natural([1]))
    den2 = Natural([4])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([4]))  
    expected_den = Natural([4])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_sub_with_zero():
    """Вычитание нулевой дроби"""
    num1 = Integer(0, Natural([2]))
    den1 = Natural([3])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([0]))
    den2 = Natural([1])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([2]))
    expected_den = Natural([3])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_sub_from_zero():
    """Вычитание из нулевой дроби"""
    num1 = Integer(0, Natural([0]))
    den1 = Natural([1])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([2]))
    den2 = Natural([3])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(1, Natural([2]))  
    expected_den = Natural([3])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_sub_zero_from_zero():
    """Вычитание нуля из нуля"""
    num1 = Integer(0, Natural([0]))
    den1 = Natural([1])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([0]))
    den2 = Natural([1])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([0]))
    expected_den = Natural([1])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits

def test_sub_large_numbers():
    """Вычитание дробей с большими числами"""
    num1 = Integer(0, Natural([7, 8, 9]))
    den1 = Natural([1, 0, 0, 0])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([1, 2, 3]))
    den2 = Natural([4, 5, 6])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    assert result.numerator.sign == 0  
    assert len(result.numerator.absolute.digits) > 0
    assert len(result.denominator.digits) > 0

def test_sub_different_denominators():
    """Вычитание дробей с разными знаменателями"""
    num1 = Integer(0, Natural([1]))
    den1 = Natural([2])
    frac1 = Rational(num1, den1)
    
    num2 = Integer(0, Natural([1]))
    den2 = Natural([3])
    frac2 = Rational(num2, den2)
    
    result = frac1.SUB_QQ_Q(frac2)
    
    expected_num = Integer(0, Natural([1]))
    expected_den = Natural([6])
    
    assert result.numerator.sign == expected_num.sign
    assert result.numerator.absolute.digits == expected_num.absolute.digits
    assert result.denominator.digits == expected_den.digits
    
