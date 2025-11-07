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
