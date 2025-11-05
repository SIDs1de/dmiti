from src.natural import Natural


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