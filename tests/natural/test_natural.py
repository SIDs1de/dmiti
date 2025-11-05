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
