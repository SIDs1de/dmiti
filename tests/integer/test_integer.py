from src.integer import Integer
from src.natural import Natural

def test_abs_z_n_returns_natural_for_all_integer_types():
    """Проверка ABS_Z_N: возврат Natural для положительных, отрицательных чисел и нуля"""
    # Положительное число
    expected = Natural([1, 2, 3])
    result = Integer(1, Natural([1, 2, 3])).abs_z_n()
    assert result.COM_NN_D(expected) == 0
    # Отрицательное число
    result = Integer(-1, Natural([4, 5])).abs_z_n()
    expected = Natural([4, 5])
    assert result.COM_NN_D(expected) == 0
    # Ноль
    result = Integer(1, Natural([0])).abs_z_n()
    expected = Natural([0])
    assert result.COM_NN_D(expected) == 0

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

def test_mul_zm_z_changes_sign_correctly():
    """Проверка MUL_ZM_Z: корректное изменение знака у целого числа"""
    # Положительное -> отрицательное
    num = Integer(0, Natural([1, 2, 3]))
    result = num.mul_zm_z()
    assert result.sign == 1
    assert result.absolute.digits == num.absolute.digits

    # Отрицательное -> положительное
    num = Integer(1, Natural([4, 5, 6]))
    result = num.mul_zm_z()
    assert result.sign == 0
    assert result.absolute.digits == num.absolute.digits

    # Ноль 
    num = Integer(0, Natural([0]))
    result = num.mul_zm_z()
    assert result.sign == 0
    assert result.absolute.digits == num.absolute.digits
