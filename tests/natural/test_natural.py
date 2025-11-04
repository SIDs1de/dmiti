from src.natural import Natural


def test_creation():
    """Тест создания чисел"""
    assert Natural([0]).digits == [0]
    assert Natural([1, 2, 3]).digits == [1, 2, 3]


def test_com_nn_d():
    """Тест сравнения чисел"""
    a = Natural([1])
    b = Natural([2])
    assert a.com_nn_d(a) == 0
    assert a.com_nn_d(b) == 1
    assert b.com_nn_d(a) == 2


def test_nzer_n_b():
    """Тест проверки на ноль"""
    assert Natural([0]).nzer_n_b() == "нет"
    assert Natural([1]).nzer_n_b() == "да"


def test_add_1n_n():
    """Тест добавления 1"""
    assert Natural([0]).add_1n_n() == Natural([1])
    assert Natural([9]).add_1n_n() == Natural([0, 1])
