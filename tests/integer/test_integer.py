from src.integer import Integer
from src.natural.base import Natural

def test_abs_z_n_returns_natural_for_all_integer_types():
    """Проверка ABS_Z_N: возврат Natural для положительных, отрицательных чисел и нуля"""
    # Положительное число
    assert Integer(1, Natural([1, 2, 3])).abs_z_n() == Natural([1, 2, 3])
    # Отрицательное число  
    assert Integer(-1, Natural([4, 5])).abs_z_n() == Natural([4, 5])
    # Ноль
    assert Integer(0, Natural([0])).abs_z_n() == Natural([0])
    # Положительный ноль
    assert Integer(1, Natural([0])).abs_z_n() == Natural([0])
    # Отрицательный ноль
    assert Integer(-1, Natural([0])).abs_z_n() == Natural([0])

def test_poz_z_d_returns_correct_sign_codes():
    """Проверка POZ_Z_D: корректные коды знака для разных типов чисел"""
    # Положительные числа
    assert Integer(1, Natural([1])).poz_z_d() == 2
    assert Integer(1, Natural([9, 9, 9])).poz_z_d() == 2
    # Отрицательные числа
    assert Integer(-1, Natural([1])).poz_z_d() == 1
    assert Integer(-1, Natural([9, 9, 9])).poz_z_d() == 1
    # Нулевые значения
    assert Integer(0, Natural([0])).poz_z_d() == 0
    assert Integer(1, Natural([0])).poz_z_d() == 0
    assert Integer(-1, Natural([0])).poz_z_d() == 0