from src.natural import Natural
from src.natural.enums import BoolResult

def test_creation():
    """Тест создания чисел"""
    assert Natural([0]).digits == [0]
    assert Natural([1, 2, 3]).digits == [1, 2, 3]

def test_equal_numbers():
    """Тест сравнения равных чисел"""
    a = Natural([1, 2, 3])
    b = Natural([1, 2, 3])
    assert a.COM_NN_D(b) == 0

def test_first_greater_by_length():
    """Тест сравнения: первое число больше по длине"""
    a = Natural([1, 2, 3, 4])
    b = Natural([1, 2, 3])
    assert a.COM_NN_D(b) == 2

def test_second_greater_by_length():
    """Тест сравнения: второе число больше по длине"""
    a = Natural([1, 2, 3])
    b = Natural([1, 2, 3, 4])
    assert a.COM_NN_D(b) == 1

def test_single_digit_comparison():
    """Тест сравнения однозначных чисел"""
    a = Natural([7])
    b = Natural([3])
    assert a.COM_NN_D(b) == 2
    assert b.COM_NN_D(a) == 1

def test_zero_vs_nonzero():
    """Тест: сравнение нуля с ненулевым числом"""
    zero = Natural([0])
    non_zero = Natural([1])
    assert zero.COM_NN_D(non_zero) == 1
    assert non_zero.COM_NN_D(zero) == 2

def test_mul_by_zero():
    """Умножение любого числа на 0"""
    a = Natural([1, 2, 3])
    result = a.MUL_ND_N(0)
    assert result.digits == [0]

def test_mul_by_one():
    """Умножение на 1 возвращает копию числа"""
    a = Natural([4, 5, 6])
    result = a.MUL_ND_N(1)
    assert result.digits == [4, 5, 6]
    assert result is not a 

def test_mul_single_digit():
    """Умножение на цифру без переноса"""
    a = Natural([1, 2, 3])  
    result = a.MUL_ND_N(2)
    assert result.digits == [2, 4, 6] 

def test_mul_with_carry():
    """Умножение с переносом"""
    a = Natural([9, 9, 9]) 
    result = a.MUL_ND_N(9)
    assert result.digits == [8, 9, 9, 1] 

def test_invalid_digit_type():
    """Ошибка при передаче нецелого значения"""
    a = Natural([1, 2, 3])
    try:
        a.MUL_ND_N("x")
        assert False
    except TypeError:
        pass

def test_invalid_digit_range():
    """Ошибка при передаче d > 9"""
    a = Natural([1, 2, 3])
    try:
        a.MUL_ND_N(12)
        assert False
    except ValueError:
        pass

def test_zero_number_returns_no():
    """Тест проверки на ноль: для числа 0 возвращает BoolResult.NO"""
    zero = Natural([0])
    result = zero.NZER_N_B()
    assert result == BoolResult.NO

def test_non_zero_single_digit_returns_yes():
    """Тест проверки на ноль: для однозначного ненулевого числа возвращает BoolResult.YES"""
    num1 = Natural([1])
    num5 = Natural([5])
    num9 = Natural([9])

    assert num1.NZER_N_B() == BoolResult.YES
    assert num5.NZER_N_B() == BoolResult.YES
    assert num9.NZER_N_B() == BoolResult.YES

def test_non_zero_multi_digit_returns_yes():
    """Тест проверки на ноль: для многозначного числа возвращает BoolResult.YES"""
    num1 = Natural([1, 0])
    num2 = Natural([1, 2, 3])
    num3 = Natural([9, 9, 9])

    assert num1.NZER_N_B() == BoolResult.YES
    assert num2.NZER_N_B() == BoolResult.YES
    assert num3.NZER_N_B() == BoolResult.YES

def test_number_with_leading_zeros_normalizes_and_returns_yes():
    """Тест проверки на ноль: число с ведущими нулями нормализуется и возвращает BoolResult.YES"""
    num1 = Natural([0, 0, 1])
    num2 = Natural([0, 5])

    assert num1.NZER_N_B() == BoolResult.YES
    assert num2.NZER_N_B() == BoolResult.YES

def test_mul_nk_n_basic_shift():
    """Тест: умножение на 10^k — проверка добавления нулей"""
    a = Natural([1,2,3])     
    r = a.MUL_Nk_N(2)        
    assert r.digits == [1,2,3,0,0]

def test_mul_nk_n_zero_number():
    """Тест: ноль при умножении остаётся нулём"""
    z = Natural([0])
    assert z.MUL_Nk_N(5).digits == [0]

def test_mul_nk_n_zero_shift():
    """Тест: умножение на 10^0 возвращает копию числа"""
    a = Natural([4,5])
    r = a.MUL_Nk_N(0)
    assert r.digits == [4,5]
    assert r is not a 

def test_mul_nk_n_invalid_k_type():
    """Тест: при неверном типе аргумента (строка вместо числа) выбрасывается TypeError"""
    a = Natural([1])
    try:
        a.MUL_Nk_N("x")
        assert False
    except TypeError:
        pass

def test_mul_nk_n_invalid_k_negative():
    """Тест: при отрицательном показателе степени выбрасывается ValueError"""
    a = Natural([1])
    try:
        a.MUL_Nk_N(-1)
        assert False
    except ValueError:
        pass