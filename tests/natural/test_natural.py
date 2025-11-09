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
	
def test_add_one_to_large_number():
	"""Тест: Добавление 1 к большому числу без переноса"""
	a = Natural([1, 2, 3, 4, 5, 6, 7, 8])
	res = a.ADD_1N_N()
	assert res.digits == [1, 2, 3, 4, 5, 6, 7, 9]

def test_add_one_with_middle_carry():
	"""Тест: Добавление 1 с переносом через середину числа"""
	a = Natural([9, 0, 9, 9])
	res = a.ADD_1N_N()
	assert res.digits == [9, 1, 0, 0]

def test_add_one_to_all_nines_prefix():
	"""Тест: Добавление 1 к числу с 9 после первой цифры"""
	a = Natural([8, 9, 9, 9])
	res = a.ADD_1N_N()
	assert res.digits == [9, 0, 0, 0]

def test_add_one_to_zero():
	"""Тест: Добавление 1 к нулю"""
	a = Natural([0])
	res = a.ADD_1N_N()
	assert res.digits == [1]

def test_add_one_all_nines():
	"""Тест: 999 + 1 = 1000"""
	a = Natural([9, 9, 9])
	res = a.ADD_1N_N()
	assert res.digits == [1, 0, 0, 0]

def test_add_nn_n_equal_length_no_carry():
    """Сложение чисел одинаковой длины без переноса"""
    a = Natural([1, 2, 3])
    b = Natural([2, 3, 4])
    result = a.ADD_NN_N(b)
    assert result.digits == [3, 5, 7]

def test_add_nn_n_equal_length_with_carry():
    """Сложение чисел одинаковой длины с переносом"""
    a = Natural([1, 5, 9])  
    b = Natural([2, 8, 7])  
    result = a.ADD_NN_N(b)
    assert result.digits == [4, 4, 6]  

def test_add_nn_n_different_length():
    """Сложение чисел разной длины"""
    a = Natural([1, 2, 3])  
    b = Natural([4, 5])    
    result = a.ADD_NN_N(b)
    assert result.digits == [1, 6, 8]  

def test_add_nn_n_with_carry_propagation():
    """Сложение с распространением переноса через несколько разрядов"""
    a = Natural([1, 9, 9])  
    b = Natural([1])      
    result = a.ADD_NN_N(b)
    assert result.digits == [2, 0, 0]  

def test_add_nn_n_with_new_digit():
    """Сложение с увеличением количества разрядов"""
    a = Natural([9, 9, 9])  
    b = Natural([1])      
    result = a.ADD_NN_N(b)
    assert result.digits == [1, 0, 0, 0] 

def test_add_nn_n_with_zero():
    """Сложение с нулем"""
    a = Natural([1, 2, 3])  
    b = Natural([0])       
    result = a.ADD_NN_N(b)
    assert result.digits == [1, 2, 3]  

def test_add_nn_n_zeros():
    """Сложение нулей"""
    a = Natural([0]) 
    b = Natural([0]) 
    result = a.ADD_NN_N(b)
    assert result.digits == [0] 

def test_add_nn_n_large_numbers():
    """Сложение больших чисел"""
    a = Natural([9, 9, 9, 9, 9, 9])  
    b = Natural([1])            
    result = a.ADD_NN_N(b)
    assert result.digits == [1, 0, 0, 0, 0, 0, 0]

def test_add_nn_n_commutative():
    """Проверка коммутативности сложения"""
    a = Natural([1, 2, 3]) 
    b = Natural([4, 5, 6]) 
    result1 = a.ADD_NN_N(b)
    result2 = b.ADD_NN_N(a)
    assert result1.digits == result2.digits

def test_add_nn_n_identity():
    """Проверка свойства идентичности (a + 0 = a)"""
    a = Natural([7, 8, 9]) 
    zero = Natural([0])  
    result = a.ADD_NN_N(zero)
    assert result.digits == a.digits

def test_mul_nn_n_simple():
    """Тест: простое умножение 123 * 45 = 5535"""
    a = Natural([1, 2, 3])
    b = Natural([4, 5])
    r = a.MUL_NN_N(b)
    assert r.digits == [5, 5, 3, 5]


def test_mul_nn_n_zero():
    """Тест: умножение на ноль даёт ноль"""
    a = Natural([1, 2, 3])
    z = Natural([0])
    assert a.MUL_NN_N(z).digits == [0]
    assert z.MUL_NN_N(a).digits == [0]


def test_mul_nn_n_by_one_and_copy():
    """Тест: умножение на 1 возвращает копию числа (не тот же объект)"""
    a = Natural([7, 8, 9])
    one = Natural([1])
    r = a.MUL_NN_N(one)
    assert r.digits == [7, 8, 9]
    assert r is not a


def test_mul_nn_n_commutative():
    """Тест: проверка коммутативности для небольших чисел"""
    a = Natural([1, 2, 3])
    b = Natural([4, 5])
    r1 = a.MUL_NN_N(b)
    r2 = b.MUL_NN_N(a)
    assert r1.digits == r2.digits


def test_mul_nn_n_carries_and_length():
    """Тест: переносы и увеличение числа разрядов 999 * 999 = 998001"""
    a = Natural([9, 9, 9])
    b = Natural([9, 9, 9])
    r = a.MUL_NN_N(b)
    assert r.digits == [9, 9, 8, 0, 0, 1]


def test_div_nn_dk_mock_case():
    """Тест: проверка алгоритма на абсолютно случайных числах"""
    a = Natural([1, 4, 8, 8])
    b = Natural([5, 2])
    assert a.DIV_NN_DK(b, 0) == 9
    assert a.DIV_NN_DK(b, 1) == 2
    assert a.DIV_NN_DK(b, 2) == 0

def test_div_nn_dk_dividend_equals_shifted_divisor():
    """Тест: делимое равно сдвинутому делителю (результат должен быть 1)"""
    a = Natural([5, 2])
    b = Natural([5, 2])
    assert a.DIV_NN_DK(b, 0) == 1

def test_div_nn_dk_dividend_less_than_divisor():
    """Тест: делимое меньше делителя (k=0, результат должен быть 0)"""
    a = Natural([3, 5])
    b = Natural([5, 2])
    assert a.DIV_NN_DK(b, 0) == 0

def test_div_nn_dk_divide_by_one():
    """Тест: деление на 1"""
    a = Natural([1, 2, 3, 4])
    b = Natural([1])
    assert a.DIV_NN_DK(b, 0) == 9
    assert a.DIV_NN_DK(b, 1) == 9
    assert a.DIV_NN_DK(b, 2) == 9
    assert a.DIV_NN_DK(b, 3) == 1

def test_div_nn_dk_single_digit_cases():
    """Тест: однозначные числа"""
    a = Natural([9])
    b = Natural([3])
    assert a.DIV_NN_DK(b, 0) == 3
    
    a = Natural([7])
    b = Natural([9])
    assert a.DIV_NN_DK(b, 0) == 0

def test_div_nn_dk_large_k_returns_zero():
    """Тест: большой k делает сдвинутый делитель больше делимого"""
    a = Natural([1, 2, 3])
    b = Natural([1])
    assert a.DIV_NN_DK(b, 10) == 0

def test_div_nn_dk_result_is_nine():
    """Тест: результат равен 9 (максимальная цифра)"""
    a = Natural([9, 9])
    b = Natural([1, 1])
    assert a.DIV_NN_DK(b, 0) == 9

def test_div_nn_dk_result_is_one():
    """Тест: результат равен 1 (минимальная ненулевая цифра)"""
    a = Natural([5, 2])
    b = Natural([5, 0])
    assert a.DIV_NN_DK(b, 0) == 1

def test_div_nn_dk_exact_division():
    """Тест: точное деление"""
    a = Natural([1, 0, 0])
    b = Natural([1, 0])
    assert a.DIV_NN_DK(b, 0) == 9
    assert a.DIV_NN_DK(b, 1) == 1

def test_div_nn_dk_with_zeros_in_dividend():
    """Тест: делимое содержит нули"""
    a = Natural([1, 0, 0, 5])
    b = Natural([1, 0])
    assert a.DIV_NN_DK(b, 0) == 9

def test_div_nn_dk_dividend_slightly_greater():
    """Тест: делимое немного больше сдвинутого делителя"""
    a = Natural([5, 3])
    b = Natural([5, 2])
    assert a.DIV_NN_DK(b, 0) == 1

def test_div_nn_dk_negative_k_raises_error():
    """Тест: отрицательный k вызывает ошибку"""
    a = Natural([1, 2, 3])
    b = Natural([1])
    try:
        a.DIV_NN_DK(b, -1)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_div_nn_dk_divide_by_zero_raises_error():
    """Тест: деление на ноль вызывает ошибку"""
    a = Natural([1, 2, 3])
    b = Natural([0])
    try:
        a.DIV_NN_DK(b, 0)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_div_nn_dk_large_numbers():
    """Тест: большие числа"""
    a = Natural([9, 9, 9, 9, 9, 9])
    b = Natural([1, 0, 0, 0])
    assert a.DIV_NN_DK(b, 0) == 9
    assert a.DIV_NN_DK(b, 1) == 9
    assert a.DIV_NN_DK(b, 2) == 9

def test_sub_nn_n_equal_numbers():
    """Вычитание равных чисел"""
    a = Natural([1, 2, 3]) 
    b = Natural([1, 2, 3]) 
    result = a.SUB_NN_N(b)
    assert result.digits == [0]  

def test_sub_nn_n_no_borrow():
    """Вычитание без заёма"""
    a = Natural([5, 4, 3])
    b = Natural([3, 2, 1])  
    result = a.SUB_NN_N(b)
    assert result.digits == [2, 2, 2]

def test_sub_nn_n_with_borrow():
    """Вычитание с заёмом"""
    a = Natural([5, 0, 0]) 
    b = Natural([1, 2, 3]) 
    result = a.SUB_NN_N(b)
    assert result.digits == [3, 7, 7] 

def test_sub_nn_n_multiple_borrows():
    """Вычитание с несколькими заёмами"""
    a = Natural([1, 0, 0, 0]) 
    b = Natural([1])       
    result = a.SUB_NN_N(b)
    assert result.digits == [9, 9, 9]

def test_sub_nn_n_different_lengths():
    """Вычитание чисел разной длины"""
    a = Natural([1, 0, 0]) 
    b = Natural([5])       
    result = a.SUB_NN_N(b)
    assert result.digits == [9, 5] 

def test_sub_nn_n_large_number_minus_small():
    """Вычитание из большого числа маленького"""
    a = Natural([9, 9, 9, 9])  
    b = Natural([9, 9, 9, 8])  
    result = a.SUB_NN_N(b)
    assert result.digits == [1]

def test_sub_nn_n_with_zero():
    """Вычитание нуля"""
    a = Natural([7, 8, 9]) 
    b = Natural([0])     
    result = a.SUB_NN_N(b)
    assert result.digits == [7, 8, 9]

def test_sub_ndn_n_simple_subtraction():
    """Простое вычитание: 100 - 20*3 = 40"""
    a = Natural([1, 0, 0])
    b = Natural([2, 0])
    result = a.SUB_NDN_N(b, 3)
    assert result.digits == [4, 0]

def test_sub_ndn_n_no_borrow():
    """Вычитание без заёма: 543 - 123*2 = 297"""
    a = Natural([5, 4, 3])
    b = Natural([1, 2, 3])
    result = a.SUB_NDN_N(b, 2)
    assert result.digits == [2, 9, 7]

def test_sub_ndn_n_with_borrow():
    """Вычитание с заёмом: 500 - 123*3 = 131"""
    a = Natural([5, 0, 0])
    b = Natural([1, 2, 3])
    result = a.SUB_NDN_N(b, 3)
    assert result.digits == [1, 3, 1]

def test_sub_ndn_n_multiply_by_zero():
    """Умножение второго числа на 0: 100 - 20*0 = 100"""
    a = Natural([1, 0, 0])
    b = Natural([2, 0])
    result = a.SUB_NDN_N(b, 0)
    assert result.digits == [1, 0, 0]

def test_sub_ndn_n_multiply_by_one():
    """Умножение второго числа на 1: 100 - 20*1 = 80"""
    a = Natural([1, 0, 0])
    b = Natural([2, 0])
    result = a.SUB_NDN_N(b, 1)
    assert result.digits == [8, 0]

def test_sub_ndn_n_exact_result():
    """Точный результат: 60 - 20*3 = 0"""
    a = Natural([6, 0])
    b = Natural([2, 0])
    result = a.SUB_NDN_N(b, 3)
    assert result.digits == [0]

def test_sub_ndn_n_single_digit():
    """Однозначные числа: 9 - 3*2 = 3"""
    a = Natural([9])
    b = Natural([3])
    result = a.SUB_NDN_N(b, 2)
    assert result.digits == [3]

def test_sub_ndn_n_large_numbers():
    """Большие числа: 10000 - 1234*7 = 1362"""
    a = Natural([1, 0, 0, 0, 0])
    b = Natural([1, 2, 3, 4])
    result = a.SUB_NDN_N(b, 7)
    assert result.digits == [1, 3, 6, 2]

def test_sub_ndn_n_multiply_by_nine():
    """Умножение на максимальную цифру: 1000 - 111*9 = 1"""
    a = Natural([1, 0, 0, 0])
    b = Natural([1, 1, 1])
    result = a.SUB_NDN_N(b, 9)
    assert result.digits == [1]

def test_sub_ndn_n_invalid_digit_negative():
    """Ошибка при отрицательной цифре"""
    a = Natural([1, 0, 0])
    b = Natural([2, 0])
    try:
        a.SUB_NDN_N(b, -1)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_sub_ndn_n_invalid_digit_too_large():
    """Ошибка при цифре больше 9"""
    a = Natural([1, 0, 0])
    b = Natural([2, 0])
    try:
        a.SUB_NDN_N(b, 10)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_sub_ndn_n_negative_result_raises_error():
    """Ошибка при отрицательном результате: 10 - 5*3 должно вызвать ошибку"""
    a = Natural([1, 0])
    b = Natural([5])
    try:
        a.SUB_NDN_N(b, 3)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_sub_ndn_n_second_greater_than_first():
    """Ошибка когда второе число, умноженное на d, больше первого"""
    a = Natural([5, 0])
    b = Natural([2, 0])
    try:
        a.SUB_NDN_N(b, 3)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_sub_ndn_n_different_lengths():
    """Числа разной длины: 1000 - 99*9 = 109"""
    a = Natural([1, 0, 0, 0])
    b = Natural([9, 9])
    result = a.SUB_NDN_N(b, 9)
    assert result.digits == [1, 0, 9]

def test_sub_ndn_n_zero_first_number():
    """Вычитание из нуля: 0 - 0*5 = 0"""
    a = Natural([0])
    b = Natural([0])
    result = a.SUB_NDN_N(b, 5)
    assert result.digits == [0]

def test_sub_ndn_n_zero_second_number():
    """Вычитание нуля, умноженного на цифру: 100 - 0*5 = 100"""
    a = Natural([1, 0, 0])
    b = Natural([0])
    result = a.SUB_NDN_N(b, 5)
    assert result.digits == [1, 0, 0] 
def test_div_nn_n_division_by_zero():
    """Деление на ноль должно вызывать ValueError"""
    a = Natural([1, 2, 3])
    b = Natural([0])
    try:
        a.DIV_NN_N(b)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_div_nn_n_dividend_less_than_divisor():
    """Деление: делимое меньше делителя"""
    a = Natural([3, 5])
    b = Natural([5, 2])
    result = a.DIV_NN_N(b)
    assert result.digits == [0]

def test_div_nn_n_dividend_equals_divisor():
    """Деление: делимое равно делителю"""
    a = Natural([1, 2, 3])
    b = Natural([1, 2, 3])
    result = a.DIV_NN_N(b)
    assert result.digits == [1]

def test_div_nn_n_simple_exact_division():
    """Простое точное деление"""
    a = Natural([1, 0, 0])
    b = Natural([1, 0])
    result = a.DIV_NN_N(b)
    assert result.digits == [1, 0]

def test_div_nn_n_single_digit_exact():
    """Точное деление однозначных чисел"""
    a = Natural([9])
    b = Natural([3])
    result = a.DIV_NN_N(b)
    assert result.digits == [3]

def test_div_nn_n_single_digit_with_remainder():
    """Деление однозначных чисел с остатком"""
    a = Natural([7])
    b = Natural([3])
    result = a.DIV_NN_N(b)
    assert result.digits == [2]

def test_div_nn_n_division_by_one():
    """Деление на единицу"""
    a = Natural([1, 2, 3, 4])
    b = Natural([1])
    result = a.DIV_NN_N(b)
    assert result.digits == [1, 2, 3, 4]

def test_div_nn_n_division_with_remainder():
    """Деление с остатком"""
    a = Natural([1, 4, 8, 8])
    b = Natural([5, 2])
    result = a.DIV_NN_N(b)
    assert result.digits == [2, 8]

def test_div_nn_n_large_numbers():
    """Деление больших чисел"""
    a = Natural([9, 9, 9, 9, 9, 9])
    b = Natural([1, 0, 0, 0])
    result = a.DIV_NN_N(b)
    assert result.digits == [9, 9, 9]

def test_div_nn_n_result_has_multiple_digits():
    """Результат деления - многозначное число"""
    a = Natural([1, 0, 0, 0, 0])
    b = Natural([1, 0, 0])
    result = a.DIV_NN_N(b)
    assert result.digits == [1, 0, 0]

def test_div_nn_n_exact_division_large():
    """Точное деление больших чисел"""
    a = Natural([5, 5, 3, 5])
    b = Natural([4, 5])
    result = a.DIV_NN_N(b)
    assert result.digits == [1, 2, 3]

def test_div_nn_n_dividend_slightly_greater():
    """Делимое немного больше делителя"""
    a = Natural([1, 0, 1])
    b = Natural([1, 0, 0])
    result = a.DIV_NN_N(b)
    assert result.digits == [1]

def test_div_nn_n_zero_dividend():
    """Деление нуля на ненулевое число"""
    a = Natural([0])
    b = Natural([5])
    result = a.DIV_NN_N(b)
    assert result.digits == [0]

def test_div_nn_n_result_is_single_digit():
    """Результат деления - одна цифра"""
    a = Natural([5, 0])
    b = Natural([2, 5])
    result = a.DIV_NN_N(b)
    assert result.digits == [2]

def test_div_nn_n_complex_division():
    """Сложное деление с несколькими разрядами в результате"""
    a = Natural([9, 9, 9, 9])
    b = Natural([9, 9])
    result = a.DIV_NN_N(b)
    assert result.digits == [1, 0, 1]

def test_div_nn_n_powers_of_ten():
    """Деление степеней десяти"""
    a = Natural([1, 0, 0, 0, 0, 0])
    b = Natural([1, 0])
    result = a.DIV_NN_N(b)
    assert result.digits == [1, 0, 0, 0, 0]

def test_mod_nn_n_zero_remainder():
    """Деление без остатка"""
    a = Natural([1, 0, 0])
    b = Natural([1, 0])
    result = a.MOD_NN_N(b)
    assert result.digits == [0]


def test_mod_nn_n_nonzero_remainder():
    """Деление с ненулевым остатком"""
    a = Natural([1, 2, 3])
    b = Natural([1, 0])
    result = a.MOD_NN_N(b)
    assert result.digits == [3]  # 123 mod 10 = 3


def test_mod_nn_n_dividend_less_than_divisor():
    """Если делимое меньше делителя — остаток равен самому делимому"""
    a = Natural([9])
    b = Natural([1, 0])
    result = a.MOD_NN_N(b)
    assert result.digits == [9]


def test_mod_nn_n_equal_numbers():
    """Если числа равны — остаток должен быть нулём"""
    a = Natural([5, 0])
    b = Natural([5, 0])
    result = a.MOD_NN_N(b)
    assert result.digits == [0]


def test_mod_nn_n_large_numbers():
    """Проверка на больших числах"""
    a = Natural([9, 9, 9, 9])
    b = Natural([9, 9])
    result = a.MOD_NN_N(b)
    assert result.digits == [0]  # 9999 mod 99 = 0


def test_mod_nn_n_division_by_one():
    """Деление на единицу"""
    a = Natural([1, 2, 3, 4])
    b = Natural([1])
    result = a.MOD_NN_N(b)
    assert result.digits == [0]


def test_mod_nn_n_zero_dividend():
    """Нулевое делимое"""
    a = Natural([0])
    b = Natural([7])
    result = a.MOD_NN_N(b)
    assert result.digits == [0]

def  test_gcf_nn_n_same_num():
    a = Natural([1, 0])
    b = Natural([1, 0])
    result = a.GCF_NN_N(b)
    assert result.digits == [1, 0]

def  test_gcf_nn_n_diff_num():
    a = Natural([1, 5])
    b = Natural([9])
    result = a.GCF_NN_N(b)
    assert result.digits == [3]

def  test_gcf_nn_n_zero():
    a = Natural([0])
    b = Natural([0])
    result = a.GCF_NN_N(b)
    assert result.digits == [0]

def test_gfc_nn_n_regular():
    a = Natural([1, 8])
    b = Natural([9])
    result = a.GCF_NN_N(b)
    assert result.digits == [9]

def test_lcm_nn_n_same_number():
    a = Natural([1, 2])
    b = Natural([1, 2])
    result = a.LCM_NN_N(b)
    assert result.digits == [1, 2]

def test_lcm_nn_n_random_number():
    a = Natural([8])
    b = Natural([1, 5])
    result = a.LCM_NN_N(b)
    assert result.digits == [1, 2, 0]

def test_lcm_nn_n_one():
    a = Natural([1])
    b = Natural([9, 9, 9, 9])
    result = a.LCM_NN_N(b)
    assert result.digits == [9, 9, 9, 9]

def test_lcm_nn_n_zero():
    a = Natural([0])
    b = Natural([2, 5])
    result = a.LCM_NN_N(b)
    assert result.digits == [0]









