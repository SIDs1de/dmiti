from src.integer import Integer
from src.natural import Natural
from src.rational import Rational
from src.polynomial import Polynomial


def test_mul_pq_p_basic():
    """Базовые тесты умножения полинома на рациональное число"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([1])), Natural([1])),   # 1 (x^0)
        Rational(Integer(0, Natural([3])), Natural([1])),   # 3x (x^1)
        Rational(Integer(0, Natural([2])), Natural([1]))    # 2x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 1/2
    multiplier = Rational(Integer(0, Natural([1])), Natural([2]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: x^2 + 3/2x + 1/2 (без сокращения: 2/2x^2 + 3/2x + 1/2)
    assert len(result.coefficients) == 3
    assert result.coefficients[0].numerator.absolute.digits == [1]  # 1/2 * 1 = 1/2
    assert result.coefficients[0].numerator.sign == 0
    assert result.coefficients[0].denominator.digits == [2]
    
    assert result.coefficients[1].numerator.absolute.digits == [3]  # 1/2 * 3 = 3/2
    assert result.coefficients[1].numerator.sign == 0
    assert result.coefficients[1].denominator.digits == [2]
    
    assert result.coefficients[2].numerator.absolute.digits == [2]  # 1/2 * 2 = 2/2 (несокращенная)
    assert result.coefficients[2].numerator.sign == 0
    assert result.coefficients[2].denominator.digits == [2]


def test_mul_pq_p_zero():
    """Тест умножения полинома на ноль"""
    # Полином: x^2 + 3x + 2 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),   # 2 (x^0)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 0
    multiplier = Rational(Integer(0, Natural([0])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Все коэффициенты должны стать нулями
    for coeff in result.coefficients:
        assert coeff.is_zero()


def test_mul_pq_p_negative():
    """Тест умножения полинома на отрицательное рациональное число"""
    # Полином: x^2 + 2x (коэффициенты от младшей степени к старшей)
    # Примечание: нулевой свободный член будет удален _validate()
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на -1/2
    multiplier = Rational(Integer(1, Natural([1])), Natural([2]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: -1/2x^2 - x (без сокращения: -2/2x - 1/2x^2)
    assert len(result.coefficients) == 2
    
    assert result.coefficients[0].numerator.absolute.digits == [2]  # 2 * (-1/2) = -2/2 (несокращенная)
    assert result.coefficients[0].numerator.sign == 1  # отрицательное
    assert result.coefficients[0].denominator.digits == [2]
    
    assert result.coefficients[1].numerator.absolute.digits == [1]  # 1 * (-1/2) = -1/2
    assert result.coefficients[1].numerator.sign == 1  # отрицательное
    assert result.coefficients[1].denominator.digits == [2]


def test_mul_pq_p_constant_polynomial():
    """Тест умножения константного полинома"""
    # Полином: 5 (константа)
    coeffs = [Rational(Integer(0, Natural([5])), Natural([1]))]
    poly = Polynomial(coeffs)
    
    # Умножаем на 3/4
    multiplier = Rational(Integer(0, Natural([3])), Natural([4]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: 15/4
    assert len(result.coefficients) == 1
    assert result.coefficients[0].numerator.absolute.digits == [1, 5]
    assert result.coefficients[0].numerator.sign == 0
    assert result.coefficients[0].denominator.digits == [4]


def test_mul_pq_p_identity():
    """Тест умножения на единицу (должно остаться без изменений)"""
    # Полином: x^2 + 3x + 2 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),   # 2 (x^0)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 1
    multiplier = Rational(Integer(0, Natural([1])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Результат должен быть равен исходному полиному
    assert len(result.coefficients) == len(poly.coefficients)
    for i in range(len(result.coefficients)):
        assert result.coefficients[i].numerator.absolute.digits == poly.coefficients[i].numerator.absolute.digits
        assert result.coefficients[i].numerator.sign == poly.coefficients[i].numerator.sign
        assert result.coefficients[i].denominator.digits == poly.coefficients[i].denominator.digits


def test_mul_pq_p_fractional_coefficients():
    """Тест умножения полинома с дробными коэффициентами"""
    # Полином: 1/4x^2 + 1/3x + 1/2 (коэффициенты от младшей степени к старшей)
    coeffs = [
        Rational(Integer(0, Natural([1])), Natural([2])),   # 1/2 (x^0)
        Rational(Integer(0, Natural([1])), Natural([3])),   # 1/3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([4]))    # 1/4x^2 (x^2)
    ]
    poly = Polynomial(coeffs)
    
    # Умножаем на 6
    multiplier = Rational(Integer(0, Natural([6])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: 3/2x^2 + 2x + 3 (без сокращения: 6/4x^2 + 6/3x + 6/2)
    assert len(result.coefficients) == 3
    assert result.coefficients[0].numerator.absolute.digits == [6]  # 1/2 * 6 = 6/2 (несокращенная)
    assert result.coefficients[0].denominator.digits == [2]
    
    assert result.coefficients[1].numerator.absolute.digits == [6]  # 1/3 * 6 = 6/3 (несокращенная)
    assert result.coefficients[1].denominator.digits == [3]
    
    assert result.coefficients[2].numerator.absolute.digits == [6]  # 1/4 * 6 = 6/4 (несокращенная)
    assert result.coefficients[2].denominator.digits == [4]


def test_mul_pq_p_immutability():
    """Тест, что исходный полином не изменяется"""
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),
        Rational(Integer(0, Natural([3])), Natural([1]))
    ]
    poly = Polynomial(coeffs)
    # Сохраняем исходные значения для проверки
    original_digits_0 = poly.coefficients[0].numerator.absolute.digits.copy()
    original_sign_0 = poly.coefficients[0].numerator.sign
    original_denom_0 = poly.coefficients[0].denominator.digits.copy()
    original_digits_1 = poly.coefficients[1].numerator.absolute.digits.copy()
    original_sign_1 = poly.coefficients[1].numerator.sign
    original_denom_1 = poly.coefficients[1].denominator.digits.copy()
    
    multiplier = Rational(Integer(0, Natural([2])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Исходный полином не должен измениться
    assert poly.coefficients[0].numerator.absolute.digits == original_digits_0
    assert poly.coefficients[0].numerator.sign == original_sign_0
    assert poly.coefficients[0].denominator.digits == original_denom_0
    assert poly.coefficients[1].numerator.absolute.digits == original_digits_1
    assert poly.coefficients[1].numerator.sign == original_sign_1
    assert poly.coefficients[1].denominator.digits == original_denom_1


def test_led_p_q_basic():
    """Базовые тесты получения старшего коэффициента полинома"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от старшей степени к младшей)
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^2 (x^2)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))  # 1 (x^0)
    ]
    poly = Polynomial(coeffs)

    # Получаем старший коэффициент
    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 2
    assert leading_coeff.numerator.absolute.digits == [2]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_single_coefficient():
    """Тест получения старшего коэффициента у константного полинома"""
    # Полином: 5 (константа)
    coeffs = [Rational(Integer(0, Natural([5])), Natural([1]))]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 5
    assert leading_coeff.numerator.absolute.digits == [5]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_fractional():
    """Тест получения дробного старшего коэффициента"""
    # Полином: 3/4x^3 + 2x^2 + 1 (коэффициенты от старшей степени к младшей)
    coeffs = [
        Rational(Integer(0, Natural([3])), Natural([4])),  # 3/4x^3 (x^3)
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^2 (x^2)
        Rational(Integer(0, Natural([1])), Natural([1]))  # 1 (x^0)
    ]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 3/4
    assert leading_coeff.numerator.absolute.digits == [3]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [4]


def test_led_p_q_negative():
    """Тест получения отрицательного старшего коэффициента"""
    # Полином: -2x^2 + 3x - 1 (коэффициенты от старшей степени к младшей)
    coeffs = [
        Rational(Integer(1, Natural([2])), Natural([1])),  # -2x^2 (x^2)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(1, Natural([1])), Natural([1]))  # -1 (x^0)
    ]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: -2
    assert leading_coeff.numerator.absolute.digits == [2]
    assert leading_coeff.numerator.sign == 1  # отрицательное
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_zero_polynomial():
    """Тест получения старшего коэффициента у нулевого полинома"""
    # Нулевой полином (после валидации останется один нулевой коэффициент)
    coeffs = [
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2 (x^2)
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x (x^1)
        Rational(Integer(0, Natural([0])), Natural([1]))  # 0 (x^0)
    ]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 0
    assert leading_coeff.is_zero()


def test_led_p_q_after_validation():
    """Тест получения старшего коэффициента после удаления ведущих нулей"""
    # Полином с ведущими нулями: 0x^3 + 0x^2 + 2x + 1 (после валидации станет 2x + 1)
    coeffs = [
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^3 (x^3)
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2 (x^2)
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))  # 1 (x^0)
    ]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # После валидации полином должен стать 2x + 1, старший коэффициент = 2
    assert len(poly.coefficients) == 2  # Проверяем, что ведущие нули удалены
    assert leading_coeff.numerator.absolute.digits == [2]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_complex_fraction():
    """Тест получения сложного дробного старшего коэффициента"""
    # Полином: 5/6x^2 + 1/3x + 1/2 (коэффициенты от старшей степени к младшей)
    coeffs = [
        Rational(Integer(0, Natural([5])), Natural([6])),  # 5/6x^2 (x^2)
        Rational(Integer(0, Natural([1])), Natural([3])),  # 1/3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([2]))  # 1/2 (x^0)
    ]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 5/6
    assert leading_coeff.numerator.absolute.digits == [5]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [6]


def test_led_p_q_immutability():
    """Тест, что исходный полином не изменяется при получении старшего коэффициента"""
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),
        Rational(Integer(0, Natural([3])), Natural([1])),
        Rational(Integer(0, Natural([1])), Natural([1]))
    ]
    poly = Polynomial(coeffs)

    # Сохраняем исходные значения для проверки
    original_digits_0 = poly.coefficients[0].numerator.absolute.digits.copy()
    original_sign_0 = poly.coefficients[0].numerator.sign
    original_denom_0 = poly.coefficients[0].denominator.digits.copy()

    # Получаем старший коэффициент
    leading_coeff = poly.LED_P_Q()

    # Исходный полином не должен измениться
    assert poly.coefficients[0].numerator.absolute.digits == original_digits_0
    assert poly.coefficients[0].numerator.sign == original_sign_0
    assert poly.coefficients[0].denominator.digits == original_denom_0

    # Проверяем, что полученный коэффициент корректен
    assert leading_coeff.numerator.absolute.digits == [2]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_large_numbers():
    """Тест с большими числами в старшем коэффициенте"""
    # Полином: 123x^2 + 45x + 67 (коэффициенты от старшей степени к младшей)
    coeffs = [
        Rational(Integer(0, Natural([1, 2, 3])), Natural([1])),  # 123x^2 (x^2)
        Rational(Integer(0, Natural([4, 5])), Natural([1])),  # 45x (x^1)
        Rational(Integer(0, Natural([6, 7])), Natural([1]))  # 67 (x^0)
    ]
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 123
    assert leading_coeff.numerator.absolute.digits == [1, 2, 3]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_deg_p_n_basic():
    """Базовые тесты получения степени полинома"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от старшей степени к младшей)
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^2 (x^2)
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))  # 1 (x^0)
    ]
    poly = Polynomial(coeffs)

    # Получаем степень полинома
    degree = poly.DEG_P_N()

    # Ожидаемый результат: 2
    assert degree.digits == [2]


def test_deg_p_n_single_coefficient():
    """Тест получения степени у константного полинома"""
    # Полином: 5 (константа)
    coeffs = [Rational(Integer(0, Natural([5])), Natural([1]))]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 0
    assert degree.digits == [0]


def test_deg_p_n_zero_polynomial():
    """Тест получения степени у нулевого полинома"""
    # Нулевой полином (после валидации останется один нулевой коэффициент)
    coeffs = [
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2 (x^2)
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x (x^1)
        Rational(Integer(0, Natural([0])), Natural([1]))  # 0 (x^0)
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 0 (для нулевого полинома)
    assert degree.digits == [0]


def test_deg_p_n_after_validation():
    """Тест получения степени после удаления ведущих нулей"""
    # Полином с ведущими нулями: 0x^3 + 0x^2 + 2x + 1 (после валидации станет 2x + 1)
    coeffs = [
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^3 (x^3)
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2 (x^2)
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        Rational(Integer(0, Natural([1])), Natural([1]))  # 1 (x^0)
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # После валидации полином должен стать 2x + 1, степень = 1
    assert len(poly.coefficients) == 2  # Проверяем, что ведущие нули удалены
    assert degree.digits == [1]


def test_deg_p_n_high_degree():
    """Тест получения высокой степени полинома"""
    # Полином: x^5 + 2x^4 + 3x^3 + 4x^2 + 5x + 6
    coeffs = [
        Rational(Integer(0, Natural([1])), Natural([1])),  # x^5
        Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^4
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x^3
        Rational(Integer(0, Natural([4])), Natural([1])),  # 4x^2
        Rational(Integer(0, Natural([5])), Natural([1])),  # 5x
        Rational(Integer(0, Natural([6])), Natural([1]))  # 6
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 5
    assert degree.digits == [5]


def test_deg_p_n_fractional_coefficients():
    """Тест получения степени полинома с дробными коэффициентами"""
    # Полином: 3/4x^3 + 1/2x^2 + 2/3x + 1/5
    coeffs = [
        Rational(Integer(0, Natural([3])), Natural([4])),  # 3/4x^3
        Rational(Integer(0, Natural([1])), Natural([2])),  # 1/2x^2
        Rational(Integer(0, Natural([2])), Natural([3])),  # 2/3x
        Rational(Integer(0, Natural([1])), Natural([5]))  # 1/5
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 3
    assert degree.digits == [3]


def test_deg_p_n_negative_coefficients():
    """Тест получения степени полинома с отрицательными коэффициентами"""
    # Полином: -2x^3 + 3x^2 - 4x + 5
    coeffs = [
        Rational(Integer(1, Natural([2])), Natural([1])),  # -2x^3
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x^2
        Rational(Integer(1, Natural([4])), Natural([1])),  # -4x
        Rational(Integer(0, Natural([5])), Natural([1]))  # 5
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 3
    assert degree.digits == [3]


def test_deg_p_n_large_degree():
    """Тест получения степени с большими числами"""
    # Полином степени 12
    coeffs = [Rational(Integer(0, Natural([1])), Natural([1]))] * 13
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 12
    assert degree.digits == [1, 2]


def test_deg_p_n_immutability():
    """Тест, что исходный полином не изменяется при получении степени"""
    coeffs = [
        Rational(Integer(0, Natural([2])), Natural([1])),
        Rational(Integer(0, Natural([3])), Natural([1])),
        Rational(Integer(0, Natural([1])), Natural([1]))
    ]
    poly = Polynomial(coeffs)

    # Сохраняем исходные значения для проверки
    original_coeffs_count = len(poly.coefficients)
    original_digits_0 = poly.coefficients[0].numerator.absolute.digits.copy()

    # Получаем степень
    degree = poly.DEG_P_N()

    # Исходный полином не должен измениться
    assert len(poly.coefficients) == original_coeffs_count
    assert poly.coefficients[0].numerator.absolute.digits == original_digits_0

    # Проверяем, что полученная степень корректа
    assert degree.digits == [2]


def test_deg_p_n_only_leading_nonzero():
    """Тест получения степени когда только старший коэффициент ненулевой"""
    # Полином: 7x^4 + 0x^3 + 0x^2 + 0x + 0
    coeffs = [
        Rational(Integer(0, Natural([7])), Natural([1])),  # 7x^4
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^3
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
        Rational(Integer(0, Natural([0])), Natural([1]))  # 0
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 4
    assert degree.digits == [4]


def test_deg_p_n_single_zero():
    """Тест получения степени полинома с единственным нулевым коэффициентом"""
    # Полином: 0
    coeffs = [Rational(Integer(0, Natural([0])), Natural([1]))]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 0
    assert degree.digits == [0]


def test_deg_p_n_complex_case():
    """Тест получения степени в сложном случае с разными коэффициентами"""
    # Полином: 1/2x^4 + 0x^3 + 0x^2 + 3x + 0
    coeffs = [
        Rational(Integer(0, Natural([1])), Natural([2])),  # 1/2x^4
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^3
        Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2
        Rational(Integer(0, Natural([3])), Natural([1])),  # 3x
        Rational(Integer(0, Natural([0])), Natural([1]))  # 0
    ]
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # После валидации полином станет 1/2x^4 + 3x, степень = 4
    assert degree.digits == [4]