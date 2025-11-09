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
    assert Integer(0, Natural([1])).poz_z_d() == 2
    assert Integer(0, Natural([9, 9, 9])).poz_z_d() == 2
    # Отрицательные числа
    assert Integer(1, Natural([1])).poz_z_d() == 1
    assert Integer(1, Natural([9, 9, 9])).poz_z_d() == 1
    # Нулевые значения
    assert Integer(0, Natural([0])).poz_z_d() == 0
    assert Integer(1, Natural([0])).poz_z_d() == 0

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

def test_trans_z_n_for_various_integer_types():
    """Проверка Trans_z_n: возврат Natural для положительных чисел и нуля, ValueError для отрицательных"""

    # Положительное число
    num = Integer(1, Natural([1, 2, 3]))
    result = num.trans_z_n()
    expected = Natural([1, 2, 3])
    assert result.COM_NN_D(expected) == 0

    # Ноль
    num = Integer(0, Natural([0]))
    result = num.trans_z_n()
    expected = Natural([0])
    assert result.COM_NN_D(expected) == 0

    # Отрицательное число — проверяем через try/except
    num = Integer(-1, Natural([1, 2, 3]))
    raised = False
    try:
        num.trans_z_n()
    except ValueError:
        raised = True
    assert raised, "Ожидается ValueError для отрицательного числа"

def test_trans_n_z_returns_integer_for_all_integer_types():
    """Проверка TRANS_N_Z: преобразование Natural в Integer"""
    # Положительное натуральное число
    expected = Natural([1, 2, 3])
    result = Integer(0, Natural([1, 2, 3])).trans_n_z()
    assert result.absolute.COM_NN_D(expected) == 0
    assert result.sign == 0

    # Другое натуральное число
    expected = Natural([4, 5])
    result = Integer(0, Natural([4, 5])).trans_n_z()
    assert result.absolute.COM_NN_D(expected) == 0
    assert result.sign == 0

    # Ноль
    expected = Natural([0])
    result = Integer(0, Natural([0])).trans_n_z()
    assert result.absolute.COM_NN_D(expected) == 0
    assert result.sign == 0

def test_add_zz_z_both_positive():
    """Проверка ADD_ZZ_Z: сложение двух положительных чисел"""
    # Простое сложение
    a = Integer(0, Natural([1, 2]))
    b = Integer(0, Natural([3, 4]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([4, 6]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Сложение с переносом
    a = Integer(0, Natural([5, 9]))
    b = Integer(0, Natural([1, 1]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([7, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Большие числа
    a = Integer(0, Natural([9, 9, 9]))
    b = Integer(0, Natural([1]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([1, 0, 0, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0

def test_add_zz_z_both_negative():
    """Проверка ADD_ZZ_Z: сложение двух отрицательных чисел"""
    # Простое сложение отрицательных
    a = Integer(1, Natural([1, 2]))
    b = Integer(1, Natural([3, 4]))
    result = a.add_zz_z(b)
    expected = Integer(1, Natural([4, 6]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Сложение с переносом
    a = Integer(1, Natural([5, 9]))
    b = Integer(1, Natural([1, 1]))
    result = a.add_zz_z(b)
    expected = Integer(1, Natural([7, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0

def test_add_zz_z_positive_and_negative():
    """Проверка ADD_ZZ_Z: сложение положительного и отрицательного чисел"""
    # Положительное больше по модулю
    a = Integer(0, Natural([5, 0]))
    b = Integer(1, Natural([2, 0]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([3, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Отрицательное больше по модулю
    a = Integer(0, Natural([2, 0]))
    b = Integer(1, Natural([5, 0]))
    result = a.add_zz_z(b)
    expected = Integer(1, Natural([3, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Равные по модулю, результат ноль
    a = Integer(0, Natural([1, 2, 3]))
    b = Integer(1, Natural([1, 2, 3]))
    result = a.add_zz_z(b)
    assert result.is_zero()
    assert result.sign == 0
    assert result.absolute.COM_NN_D(Natural([0])) == 0

def test_add_zz_z_negative_and_positive():
    """Проверка ADD_ZZ_Z: сложение отрицательного и положительного чисел"""
    # Отрицательное больше по модулю
    a = Integer(1, Natural([5, 0]))
    b = Integer(0, Natural([2, 0]))
    result = a.add_zz_z(b)
    expected = Integer(1, Natural([3, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Положительное больше по модулю
    a = Integer(1, Natural([2, 0]))
    b = Integer(0, Natural([5, 0]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([3, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0

def test_add_zz_z_with_zero():
    """Проверка ADD_ZZ_Z: сложение с нулем"""
    zero = Integer(0, Natural([0]))
    
    # Ноль + положительное
    a = Integer(0, Natural([1, 2, 3]))
    result = zero.add_zz_z(a)
    expected = Integer(0, Natural([1, 2, 3]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Положительное + ноль
    result = a.add_zz_z(zero)
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Ноль + отрицательное
    a = Integer(1, Natural([4, 5, 6]))
    result = zero.add_zz_z(a)
    expected = Integer(1, Natural([4, 5, 6]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Отрицательное + ноль
    result = a.add_zz_z(zero)
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Ноль + ноль
    result = zero.add_zz_z(zero)
    assert result.is_zero()
    assert result.sign == 0
    assert result.absolute.COM_NN_D(Natural([0])) == 0

def test_add_zz_z_edge_cases():
    """Проверка ADD_ZZ_Z: граничные случаи"""
    # Единица + единица
    a = Integer(0, Natural([1]))
    b = Integer(0, Natural([1]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([2]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Минус единица + минус единица
    a = Integer(1, Natural([1]))
    b = Integer(1, Natural([1]))
    result = a.add_zz_z(b)
    expected = Integer(1, Natural([2]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Большое число + маленькое
    a = Integer(0, Natural([9, 9, 9, 9, 9]))
    b = Integer(0, Natural([1]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([1, 0, 0, 0, 0, 0]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
    
    # Разные длины чисел
    a = Integer(0, Natural([1, 0, 0]))
    b = Integer(1, Natural([9, 9]))
    result = a.add_zz_z(b)
    expected = Integer(0, Natural([1]))
    assert result.sign == expected.sign
    assert result.absolute.COM_NN_D(expected.absolute) == 0
