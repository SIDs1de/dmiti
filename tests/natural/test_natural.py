from src.natural import Natural

# === ADD_1N_N ===
def test_add_one_to_large_number():
    """Добавление 1 к большому числу без переноса"""
    a = Natural([1, 2, 3, 4, 5, 6, 7, 8])
    res = a.ADD_1N_N()
    assert res.digits == [1, 2, 3, 4, 5, 6, 7, 9]

def test_add_one_with_middle_carry():
    """Добавление 1 с переносом через середину числа"""
    a = Natural([9, 0, 9, 9])
    res = a.ADD_1N_N()
    assert res.digits == [9, 1, 0, 0]

def test_add_one_to_all_nines_prefix():
    """Добавление 1 к числу с 9 после первой цифры"""
    a = Natural([8, 9, 9, 9])
    res = a.ADD_1N_N()
    assert res.digits == [9, 0, 0, 0]

def test_add_one_to_zero():
    """Добавление 1 к нулю"""
    a = Natural([0])
    res = a.ADD_1N_N()
    assert res.digits == [1]

def test_add_one_all_nines():
    """Добавление 1 к числу 999"""
    a = Natural([9, 9, 9])
    res = a.ADD_1N_N()
    assert res.digits == [1, 0, 0, 0]
    
'''
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
>>>>>>> 0bd7f5c98ab21509fb5a877b9e9fae92eb4f31f5
'''