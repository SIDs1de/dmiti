from src.integer import Integer
from src.natural import Natural


def test_abs_z_n():
    """Граничные случаи для ABS_Z_N"""
    # Ноль
    assert Integer(0, Natural([0])).abs_z_n() == Natural([0])
    # Положительное число
    assert Integer(1, Natural([1, 2, 3])).abs_z_n() == Natural([1, 2, 3])
    # Отрицательное число
    assert Integer(-1, Natural([4, 5])).abs_z_n() == Natural([4, 5])


def test_poz_z_d():
    """Граничные случаи для POZ_Z_D"""
    # Ноль
    assert Integer(0, Natural([0])).poz_z_d() == 0
    # Положительное число
    assert Integer(1, Natural([1])).poz_z_d() == 2
    # Отрицательное число
    assert Integer(-1, Natural([1])).poz_z_d() == 1