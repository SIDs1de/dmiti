from src.integer import Integer
from src.natural import Natural
from src.rational import Rational
from src.polynomial import Polynomial


def test_mul_pq_p_basic():
    """Базовые тесты умножения полинома на рациональное число"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от младшей степени к старшей)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # 1 (x^0)
        1: Rational(Integer(0, Natural([3])), Natural([1])),   # 3x (x^1)
        2: Rational(Integer(0, Natural([2])), Natural([1]))    # 2x^2 (x^2)
    }
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
    coeffs = {
        0: Rational(Integer(0, Natural([2])), Natural([1])),   # 2 (x^0)
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    }
    poly = Polynomial(coeffs)
    
    # Умножаем на 0
    multiplier = Rational(Integer(0, Natural([0])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Все коэффициенты должны стать нулями
    for coeff in result.coefficients.values():
        assert coeff.is_zero()


def test_mul_pq_p_negative():
    """Тест умножения полинома на отрицательное рациональное число"""
    # Полином: x^2 + 2x (коэффициенты от младшей степени к старшей)
    # Примечание: нулевой свободный член будет удален _validate()
    coeffs = {
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    }
    poly = Polynomial(coeffs)
    
    # Умножаем на -1/2
    multiplier = Rational(Integer(1, Natural([1])), Natural([2]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Ожидаемый результат: -1/2x^2 - x (без сокращения: -2/2x - 1/2x^2)
    assert len(result.coefficients) == 2
    
    assert result.coefficients[1].numerator.absolute.digits == [2]  # 2 * (-1/2) = -2/2 (несокращенная)
    assert result.coefficients[1].numerator.sign == 1  # отрицательное
    assert result.coefficients[1].denominator.digits == [2]
    
    assert result.coefficients[2].numerator.absolute.digits == [1]  # 1 * (-1/2) = -1/2
    assert result.coefficients[2].numerator.sign == 1  # отрицательное
    assert result.coefficients[2].denominator.digits == [2]


def test_mul_pq_p_constant_polynomial():
    """Тест умножения константного полинома"""
    # Полином: 5 (константа)
    coeffs = {0: Rational(Integer(0, Natural([5])), Natural([1]))}
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
    coeffs = {
        0: Rational(Integer(0, Natural([2])), Natural([1])),   # 2 (x^0)
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x^2 (x^2)
    }
    poly = Polynomial(coeffs)
    
    # Умножаем на 1
    multiplier = Rational(Integer(0, Natural([1])), Natural([1]))
    result = poly.MUL_PQ_P(multiplier)
    
    # Результат должен быть равен исходному полиному
    assert len(result.coefficients) == len(poly.coefficients)
    for i in result.coefficients.keys():
        assert result.coefficients[i].numerator.absolute.digits == poly.coefficients[i].numerator.absolute.digits
        assert result.coefficients[i].numerator.sign == poly.coefficients[i].numerator.sign
        assert result.coefficients[i].denominator.digits == poly.coefficients[i].denominator.digits


def test_mul_pq_p_fractional_coefficients():
    """Тест умножения полинома с дробными коэффициентами"""
    # Полином: 1/4x^2 + 1/3x + 1/2 (коэффициенты от младшей степени к старшей)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([2])),   # 1/2 (x^0)
        1: Rational(Integer(0, Natural([1])), Natural([3])),   # 1/3x (x^1)
        2: Rational(Integer(0, Natural([1])), Natural([4]))    # 1/4x^2 (x^2)
    }
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
    coeffs = {
        0: Rational(Integer(0, Natural([2])), Natural([1])),
        1: Rational(Integer(0, Natural([3])), Natural([1]))
    }
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


def test_sub_pp_p_same_polynomials():
    """Тест на проверку работоспособности с обычными значениями"""
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),
        1: Rational(Integer(0, Natural([2])), Natural([1])),
        2: Rational(Integer(0, Natural([1])), Natural([1]))
    }

    poly = Polynomial(coeffs)
    result = poly.SUB_PP_P(poly)

    assert result.coefficients[0].numerator.absolute.digits == [0]
    assert result.coefficients[0].denominator.digits == [1]


def test_sub_pp_p_different_degrees():
    """Тест вычитания многочленов разной степени"""
    poly1 = Polynomial({
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x^2
    })

    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1])),  # 0
        2: Rational(Integer(0, Natural([1])), Natural([1])),  # x^2
        3: Rational(Integer(0, Natural([3])), Natural([1]))   # 3x^3
    })

    result = poly1.SUB_PP_P(poly2)

    assert result.coefficients[3].numerator.sign == 1
    assert result.coefficients[3].numerator.absolute.digits == [3]


def test_sub_pp_p_negative_coefficients():
    """Тест на отрицательные коэффициенты"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([5])), Natural([1])),   # +5
        1: Rational(Integer(1, Natural([2])), Natural([1]))  # −2x
    })
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # +1
        1: Rational(Integer(1, Natural([3])), Natural([1]))  # −3x
    })

    result = poly1.SUB_PP_P(poly2)

    # Проверяем, что коэффициенты равны 1 и 4
    assert result.coefficients[1].numerator.sign == 0
    assert result.coefficients[1].numerator.absolute.digits == [1]
    assert result.coefficients[0].numerator.absolute.digits == [4]


def test_sub_pp_p_zero_minus_poly():
    """Тест 0 − P = −P"""
    zero_poly = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1]))  # 0
    })
    poly = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([1])),   # 3
        1: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x
    })

    result = zero_poly.SUB_PP_P(poly)

    # Ожидаем, что оба коэффициента отрицательные
    for coef in result.coefficients.values():
        assert coef.numerator.sign == 1


def test_sub_pp_p_poly_minus_zero():
    """Тест P − 0 = P"""
    poly = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([1])),
        1: Rational(Integer(0, Natural([2])), Natural([1]))
    })
    zero_poly = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1]))
    })

    result = poly.SUB_PP_P(zero_poly)

    # Проверяем, что результат совпадает с исходным
    for key in result.coefficients.keys():
        assert result.coefficients[key].numerator.absolute.digits == poly.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == poly.coefficients[key].denominator.digits


def test_sub_pp_p_fractional_coefficients():
    """Тест работы с дробными коэффициентами"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([4])),   # 3/4
        1: Rational(Integer(0, Natural([1])), Natural([2]))  # 1/2 x
    })
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([4])),   # 1/4
        1: Rational(Integer(0, Natural([1])), Natural([3]))  # 1/3 x
    })

    result = poly1.SUB_PP_P(poly2)

    assert result.coefficients[1].numerator.absolute.digits == [1]
    assert result.coefficients[1].denominator.digits == [6]
    assert result.coefficients[0].numerator.absolute.digits == [2]
    assert result.coefficients[0].denominator.digits == [4]


def test_led_p_q_basic():
    """Базовые тесты получения старшего коэффициента полинома"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от старшей степени к младшей)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),  # 1 (x^0)
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        2: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x^2 (x^2)
    }
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
    coeffs = {0: Rational(Integer(0, Natural([5])), Natural([1]))}
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 5
    assert leading_coeff.numerator.absolute.digits == [5]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_fractional():
    """Тест получения дробного старшего коэффициента"""
    # Полином: 3/4x^3 + 2x^2 + 1 (коэффициенты от старшей степени к младшей)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),  # 1 (x^0)
        2: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^2 (x^2)
        3: Rational(Integer(0, Natural([3])), Natural([4]))  # 3/4x^3 (x^3)
    }
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 3/4
    assert leading_coeff.numerator.absolute.digits == [3]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [4]


def test_led_p_q_negative():
    """Тест получения отрицательного старшего коэффициента"""
    # Полином: -2x^2 + 3x - 1 (коэффициенты от старшей степени к младшей)
    coeffs = {
        0: Rational(Integer(1, Natural([1])), Natural([1])),  # -1 (x^0)
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        2: Rational(Integer(1, Natural([2])), Natural([1]))  # -2x^2 (x^2)
    }
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: -2
    assert leading_coeff.numerator.absolute.digits == [2]
    assert leading_coeff.numerator.sign == 1  # отрицательное
    assert leading_coeff.denominator.digits == [1]


def test_led_p_q_zero_polynomial():
    """Тест получения старшего коэффициента у нулевого полинома"""
    # Нулевой полином (после валидации останется один нулевой коэффициент)
    coeffs = {
        0: Rational(Integer(0, Natural([0])), Natural([1])),  # 0 (x^0)
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x (x^1)
        2: Rational(Integer(0, Natural([0])), Natural([1]))  # 0x^2 (x^2)
    }
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 0
    assert leading_coeff.is_zero()


def test_led_p_q_after_validation():
    """Тест получения старшего коэффициента после удаления ведущих нулей"""
    # Полином с ведущими нулями: 0x^3 + 0x^2 + 2x + 1 (после валидации станет 2x + 1)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),  # 1 (x^0)
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        2: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2 (x^2)
        3: Rational(Integer(0, Natural([0])), Natural([1]))  # 0x^3 (x^3)
    }
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
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([2])),  # 1/2 (x^0)
        1: Rational(Integer(0, Natural([1])), Natural([3])),  # 1/3x (x^1)
        2: Rational(Integer(0, Natural([5])), Natural([6]))  # 5/6x^2 (x^2)
    }
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 5/6
    assert leading_coeff.numerator.absolute.digits == [5]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [6]


def test_led_p_q_immutability():
    """Тест, что исходный полином не изменяется при получении старшего коэффициента"""
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),
        1: Rational(Integer(0, Natural([3])), Natural([1])),
        2: Rational(Integer(0, Natural([2])), Natural([1]))
    }
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
    coeffs = {
        0: Rational(Integer(0, Natural([6, 7])), Natural([1])),  # 67 (x^0)
        1: Rational(Integer(0, Natural([4, 5])), Natural([1])),  # 45x (x^1)
        2: Rational(Integer(0, Natural([1, 2, 3])), Natural([1]))  # 123x^2 (x^2)
    }
    poly = Polynomial(coeffs)

    leading_coeff = poly.LED_P_Q()

    # Ожидаемый результат: 123
    assert leading_coeff.numerator.absolute.digits == [1, 2, 3]
    assert leading_coeff.numerator.sign == 0
    assert leading_coeff.denominator.digits == [1]


def test_deg_p_n_basic():
    """Базовые тесты получения степени полинома"""
    # Полином: 2x^2 + 3x + 1 (коэффициенты от старшей степени к младшей)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),  # 1 (x^0)
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x (x^1)
        2: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x^2 (x^2)
    }
    poly = Polynomial(coeffs)

    # Получаем степень полинома
    degree = poly.DEG_P_N()

    # Ожидаемый результат: 2
    assert degree.digits == [2]


def test_deg_p_n_single_coefficient():
    """Тест получения степени у константного полинома"""
    # Полином: 5 (константа)
    coeffs = {0: Rational(Integer(0, Natural([5])), Natural([1]))}
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 0
    assert degree.digits == [0]


def test_deg_p_n_zero_polynomial():
    """Тест получения степени у нулевого полинома"""
    # Нулевой полином (после валидации останется один нулевой коэффициент)
    coeffs = {
        0: Rational(Integer(0, Natural([0])), Natural([1])),  # 0 (x^0)
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x (x^1)
        2: Rational(Integer(0, Natural([0])), Natural([1]))  # 0x^2 (x^2)
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 0 (для нулевого полинома)
    assert degree.digits == [0]


def test_deg_p_n_after_validation():
    """Тест получения степени после удаления ведущих нулей"""
    # Полином с ведущими нулями: 0x^3 + 0x^2 + 2x + 1 (после валидации станет 2x + 1)
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),  # 1 (x^0)
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x (x^1)
        2: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2 (x^2)
        3: Rational(Integer(0, Natural([0])), Natural([1]))  # 0x^3 (x^3)
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # После валидации полином должен стать 2x + 1, степень = 1
    assert len(poly.coefficients) == 2  # Проверяем, что ведущие нули удалены
    assert degree.digits == [1]


def test_deg_p_n_high_degree():
    """Тест получения высокой степени полинома"""
    # Полином: x^5 + 2x^4 + 3x^3 + 4x^2 + 5x + 6
    coeffs = {
        0: Rational(Integer(0, Natural([6])), Natural([1])),  # 6
        1: Rational(Integer(0, Natural([5])), Natural([1])),  # 5x
        2: Rational(Integer(0, Natural([4])), Natural([1])),  # 4x^2
        3: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x^3
        4: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^4
        5: Rational(Integer(0, Natural([1])), Natural([1]))  # x^5
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 5
    assert degree.digits == [5]


def test_deg_p_n_fractional_coefficients():
    """Тест получения степени полинома с дробными коэффициентами"""
    # Полином: 3/4x^3 + 1/2x^2 + 2/3x + 1/5
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([5])),  # 1/5
        1: Rational(Integer(0, Natural([2])), Natural([3])),  # 2/3x
        2: Rational(Integer(0, Natural([1])), Natural([2])),  # 1/2x^2
        3: Rational(Integer(0, Natural([3])), Natural([4]))  # 3/4x^3
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 3
    assert degree.digits == [3]


def test_deg_p_n_negative_coefficients():
    """Тест получения степени полинома с отрицательными коэффициентами"""
    # Полином: -2x^3 + 3x^2 - 4x + 5
    coeffs = {
        0: Rational(Integer(0, Natural([5])), Natural([1])),  # 5
        1: Rational(Integer(1, Natural([4])), Natural([1])),  # -4x
        2: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x^2
        3: Rational(Integer(1, Natural([2])), Natural([1]))  # -2x^3
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 3
    assert degree.digits == [3]


def test_deg_p_n_large_degree():
    """Тест получения степени с большими числами"""
    # Полином степени 12
    coeffs = {i: Rational(Integer(0, Natural([1])), Natural([1])) for i in range(13)}
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 12
    assert degree.digits == [1, 2]


def test_deg_p_n_immutability():
    """Тест, что исходный полином не изменяется при получении степени"""
    coeffs = {
        0: Rational(Integer(0, Natural([1])), Natural([1])),
        1: Rational(Integer(0, Natural([3])), Natural([1])),
        2: Rational(Integer(0, Natural([2])), Natural([1]))
    }
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
    coeffs = {
        0: Rational(Integer(0, Natural([0])), Natural([1])),  # 0
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
        2: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2
        3: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^3
        4: Rational(Integer(0, Natural([7])), Natural([1]))  # 7x^4
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 4
    assert degree.digits == [4]


def test_deg_p_n_single_zero():
    """Тест получения степени полинома с единственным нулевым коэффициентом"""
    # Полином: 0
    coeffs = {0: Rational(Integer(0, Natural([0])), Natural([1]))}
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # Ожидаемый результат: 0
    assert degree.digits == [0]


def test_deg_p_n_complex_case():
    """Тест получения степени в сложном случае с разными коэффициентами"""
    # Полином: 1/2x^4 + 0x^3 + 0x^2 + 3x + 0
    coeffs = {
        0: Rational(Integer(0, Natural([0])), Natural([1])),  # 0
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x
        2: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^2
        3: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x^3
        4: Rational(Integer(0, Natural([1])), Natural([2]))  # 1/2x^4
    }
    poly = Polynomial(coeffs)

    degree = poly.DEG_P_N()

    # После валидации полином станет 1/2x^4 + 3x, степень = 4
    assert degree.digits == [4]

def test_mul_pxk_p_zero_k():
    """Умножение на x^0 - полином не должен измениться"""
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),
        1: Rational(Integer(0, Natural([2])), Natural([1])),
        2: Rational(Integer(0, Natural([1])), Natural([1]))
    }
    poly = Polynomial(coeffs)
    k = Natural([0])
    result = poly.MUL_Pxk_P(k)
    
    # Проверяем что коэффициенты не изменились
    assert len(result.coefficients) == 3
    assert result.coefficients[0].numerator.absolute.digits == [3]
    assert result.coefficients[1].numerator.absolute.digits == [2]
    assert result.coefficients[2].numerator.absolute.digits == [1]

def test_mul_pxk_p_basic():
    """Базовое умножение на x^2"""
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),   # x^0
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # x^1
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x^2
    }
    poly = Polynomial(coeffs)
    k = Natural([2])
    result = poly.MUL_Pxk_P(k)

    # Должно стать: 1*x^4 + 2*x^3 + 3*x^2
    assert len(result.coefficients) == 3
    # Проверяем коэффициенты
    assert result.coefficients[2].numerator.absolute.digits == [3]  # x^2 -> x^4
    assert result.coefficients[3].numerator.absolute.digits == [2]  # x^1 -> x^3
    assert result.coefficients[4].numerator.absolute.digits == [1]  # x^0 -> x^2
    
def test_mul_pxk_p_single_coeff():
    """Умножение полинома с одним коэффициентом"""
    coeffs = {0: Rational(Integer(0, Natural([5])), Natural([1]))}  # 5
    poly = Polynomial(coeffs)
    k = Natural([3])
    result = poly.MUL_Pxk_P(k)

    # Должно стать: 5*x^3
    assert len(result.coefficients) == 1
    assert result.coefficients[3].numerator.absolute.digits == [5]  # x^0 -> x^3
    
def test_mul_pxk_p_zero_polynomial():
    """Умножение нулевого полинома"""
    coeffs = {0: Rational(Integer(0, Natural([0])), Natural([1]))}  # 0
    poly = Polynomial(coeffs)
    k = Natural([2])
    result = poly.MUL_Pxk_P(k)
    
    # Нулевой полином после умножения останется нулевым
    # После валидации нулевой полином остается {0: 0}
    assert len(result.coefficients) == 1
    assert 0 in result.coefficients
    assert result.coefficients[0].numerator.absolute.digits == [0]

def test_mul_pxk_p_large_k():
    """Умножение на большое k (k=10)"""
    coeffs = {
        0: Rational(Integer(0, Natural([2])), Natural([1])),   # x^0
        1: Rational(Integer(0, Natural([1])), Natural([1]))  # x^1
    }
    poly = Polynomial(coeffs)
    k = Natural([1, 0])  # k = 10
    result = poly.MUL_Pxk_P(k)

    # Должно быть: 1*x^11 + 2*x^10
    assert len(result.coefficients) == 2
    # Первые 2 коэффициента - исходные
    assert result.coefficients[10].numerator.absolute.digits == [2]  # x^0 -> x^10
    assert result.coefficients[11].numerator.absolute.digits == [1]  # x^1 -> x^11
        
def test_mul_pxk_p_negative_coeffs():
    """Умножение полинома с отрицательными коэффициентами"""
    coeffs = {
        0: Rational(Integer(0, Natural([2])), Natural([1])),   # +2*x^0
        1: Rational(Integer(1, Natural([1])), Natural([1]))  # -1*x^1
    }
    poly = Polynomial(coeffs)
    k = Natural([1])
    result = poly.MUL_Pxk_P(k)

    # Должно стать: -1*x^2 + 2*x^1
    assert len(result.coefficients) == 2
    assert result.coefficients[1].numerator.sign == 0  # 2*x^1
    assert result.coefficients[1].numerator.absolute.digits == [2]
    assert result.coefficients[2].numerator.sign == 1  # -1*x^2
    assert result.coefficients[2].numerator.absolute.digits == [1]
    
def test_fac_p_q_basic_positive_integers():
    """Тест FAC_P_Q с положительными целыми коэффициентами."""
    # Полином: 6x^2 + 9x + 3
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),   # 3
        1: Rational(Integer(0, Natural([9])), Natural([1])),  # 9x
        2: Rational(Integer(0, Natural([6])), Natural([1]))  # 6x^2
    }
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # НОД(6, 9, 3) = 3, НОК(1, 1, 1) = 1
    expected_factor = Rational(Integer(0, Natural([3])), Natural([1]))
    assert str(factor) == str(expected_factor)


def test_fac_p_q_with_zero_coefficient():
    """Тест FAC_P_Q с нулевым коэффициентом."""
    # Полином: 6x^2 + 0x + 3
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),   # 3
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
        2: Rational(Integer(0, Natural([6])), Natural([1]))  # 6x^2
    }
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # НОД(6, 3) = 3 (0 игнорируется), НОК(1, 1, 1) = 1
    expected_factor = Rational(Integer(0, Natural([3])), Natural([1]))
    assert str(factor) == str(expected_factor)


def test_fac_p_q_fractional_coefficients():
    """Тест FAC_P_Q с дробными коэффициентами."""
    # Полином: (4/6)x^2 + (8/12)x + (2/3)
    # Упрощённо: (2/3)x^2 + (2/3)x + (2/3)
    coeffs = {
        0: Rational(Integer(0, Natural([2])), Natural([3])),    # 2/3
        1: Rational(Integer(0, Natural([8])), Natural([1,2])),  # 8/12 x
        2: Rational(Integer(0, Natural([4])), Natural([6]))   # 4/6 x^2
    }
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # НОД числителей (4, 8, 2) = 2, НОК знаменателей (6, 12, 3) = 12
    expected_factor = Rational(Integer(0, Natural([2])), Natural([1,2]))
    assert str(factor) == str(expected_factor)


def test_fac_p_q_negative_coefficients():
    """Тест FAC_P_Q с отрицательными коэффициентами."""
    # Полином: -12x^2 + 18x - 6
    coeffs = {
        0: Rational(Integer(1, Natural([6])), Natural([1])),    # -6
        1: Rational(Integer(0, Natural([1,8])), Natural([1])),  # 18x
        2: Rational(Integer(1, Natural([1,2])), Natural([1]))  # -12x^2
    }
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # НОД(12, 18, 6) = 6, НОК(1, 1, 1) = 1
    # Знак НОД определяется по первому ненулевому коэффициенту (в данном случае положительный НОД)
    # Результат: 6/1, но знак определяется логикой алгоритма (НОД всегда положительный)
    expected_factor = Rational(Integer(0, Natural([6])), Natural([1]))
    assert str(factor) == str(expected_factor)


def test_fac_p_q_all_zero_polynomial():
    """Тест FAC_P_Q с нулевым полиномом."""
    # Полином: 0x^2 + 0x + 0
    coeffs = {
        0: Rational(Integer(0, Natural([0])), Natural([1])),
        1: Rational(Integer(0, Natural([0])), Natural([1])),
        2: Rational(Integer(0, Natural([0])), Natural([1]))
    }
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # Ожидаем 1/1 для нулевого полинома
    expected_factor = Rational(Integer(0, Natural([1])), Natural([1]))
    assert str(factor) == str(expected_factor)


def test_fac_p_q_single_coefficient():
    """Тест FAC_P_Q с полиномом из одного коэффициента."""
    # Полином: 7 (или 7x^0)
    coeffs = {0: Rational(Integer(0, Natural([7])), Natural([1]))}
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # НОД(7) = 7, НОК(1) = 1
    expected_factor = Rational(Integer(0, Natural([7])), Natural([1]))
    assert str(factor) == str(expected_factor)


def test_fac_p_q_mixed_int_and_frac():
    """Тест FAC_P_Q со смешанными целыми и дробными коэффициентами."""
    # Полином: 15x^3 + (10/5)x^2 + (6/3)x + 3
    # Упрощённо: 15x^3 + 2x^2 + 2x + 3
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),     # 3
        1: Rational(Integer(0, Natural([6])), Natural([3])),    # (6/3)x
        2: Rational(Integer(0, Natural([1,0])), Natural([5])),   # (10/5)x^2
        3: Rational(Integer(0, Natural([1,5])), Natural([1]))   # 15x^3
    }
    poly = Polynomial(coeffs)

    factor = poly.FAC_P_Q()

    # НОД(15, 10, 6, 3) = 1, НОК(1, 5, 3, 1) = 15
    expected_factor = Rational(Integer(0, Natural([1])), Natural([1,5]))
    assert str(factor) == str(expected_factor)

def test_add_pp_p_same_polynomials():
    """Тест на проверку сложения одинаковых многочленов"""
    coeffs = {
        0: Rational(Integer(0, Natural([3])), Natural([1])),
        1: Rational(Integer(0, Natural([2])), Natural([1])),
        2: Rational(Integer(0, Natural([1])), Natural([1]))
    }

    poly = Polynomial(coeffs)
    result = poly.ADD_PP_P(poly)

    # Проверяем, что коэффициенты удвоились
    assert result.coefficients[0].numerator.absolute.digits == [6]
    assert result.coefficients[1].numerator.absolute.digits == [4]
    assert result.coefficients[2].numerator.absolute.digits == [2]


def test_add_pp_p_example():
    """Тест сложения полиномов: 5x^2 + x + 0 и 3x^3 + 2x^2 + 0x + 4"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1])),   # 0
        1: Rational(Integer(0, Natural([1])), Natural([1])),  # 1x
        2: Rational(Integer(0, Natural([5])), Natural([1])),  # 5x^2
        3: Rational(Integer(0, Natural([0])), Natural([1]))   # 0x^3
    })

    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([4])), Natural([1])),   # 4
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
        2: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x^2
        3: Rational(Integer(0, Natural([3])), Natural([1]))   # 3x^3
    })

    result = poly1.ADD_PP_P(poly2)

    # Проверяем результат: 3x^3 + 7x^2 + 1x + 4
    assert result.coefficients[3].numerator.sign == 0
    assert result.coefficients[3].numerator.absolute.digits == [3]

    assert result.coefficients[2].numerator.sign == 0
    assert result.coefficients[2].numerator.absolute.digits == [7]

    assert result.coefficients[1].numerator.sign == 0
    assert result.coefficients[1].numerator.absolute.digits == [1]

    assert result.coefficients[0].numerator.sign == 0
    assert result.coefficients[0].numerator.absolute.digits == [4]

def test_add_pp_p_negative_coefficients():
    """Тест сложения многочленов с отрицательными коэффициентами"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([5])), Natural([1])),   # +5
        1: Rational(Integer(1, Natural([2])), Natural([1]))  # −2x
    })
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # +1
        1: Rational(Integer(1, Natural([3])), Natural([1]))  # −3x
    })

    result = poly1.ADD_PP_P(poly2)

    # (−2x) + (−3x) = −5x
    assert result.coefficients[1].numerator.sign == 1
    assert result.coefficients[1].numerator.absolute.digits == [5]

    # 5 + 1 = 6
    assert result.coefficients[0].numerator.sign == 0
    assert result.coefficients[0].numerator.absolute.digits == [6]


def test_add_pp_p_zero_plus_poly():
    """Тест 0 + P = P"""
    zero_poly = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1]))  # 0
    })
    poly = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([1])),   # 3
        1: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x
    })

    result = zero_poly.ADD_PP_P(poly)

    for key in result.coefficients.keys():
        assert result.coefficients[key].numerator.absolute.digits == poly.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == poly.coefficients[key].denominator.digits


def test_add_pp_p_poly_plus_zero():
    """Тест P + 0 = P"""
    poly = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([1])),
        1: Rational(Integer(0, Natural([2])), Natural([1]))
    })
    zero_poly = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1]))
    })

    result = poly.ADD_PP_P(zero_poly)

    for key in result.coefficients.keys():
        assert result.coefficients[key].numerator.absolute.digits == poly.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == poly.coefficients[key].denominator.digits


def test_add_pp_p_fractional_coefficients():
    """Тест работы с дробными коэффициентами"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([4])),   # 3/4
        1: Rational(Integer(0, Natural([1])), Natural([2]))  # 1/2 x
    })
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([4])),   # 1/4
        1: Rational(Integer(0, Natural([1])), Natural([3]))  # 1/3 x
    })

    result = poly1.ADD_PP_P(poly2)

    # (1/2 + 1/3) = 5/6
    assert result.coefficients[1].numerator.absolute.digits == [5]
    assert result.coefficients[1].denominator.digits == [6]

    # (3/4 + 1/4) = 4/4 (без сокращения)
    assert result.coefficients[0].numerator.absolute.digits == [4]
    assert result.coefficients[0].denominator.digits == [4]

def test_mul_constant_polynomials():
    """Умножение двух константных многочленов"""
    poly1 = Polynomial({0: Rational(Integer(0, Natural([2])), Natural([1]))})  # 2
    poly2 = Polynomial({0: Rational(Integer(0, Natural([3])), Natural([1]))})  # 3
    result = poly1.MUL_PP_P(poly2)
    
    expected = Polynomial({0: Rational(Integer(0, Natural([6])), Natural([1]))})  # 6
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits

def test_mul_with_zero_polynomial():
    """Умножение многочлена на нулевой многочлен"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x
    })  # 2x + 1
    poly2 = Polynomial({0: Rational(Integer(0, Natural([0])), Natural([1]))})  # 0
    result = poly1.MUL_PP_P(poly2)
    
    expected = Polynomial({0: Rational(Integer(0, Natural([0])), Natural([1]))})  # 0
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits

def test_mul_linear_with_constant():
    """Умножение линейного многочлена на константу"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x
    })  # 2x + 1
    poly2 = Polynomial({0: Rational(Integer(0, Natural([3])), Natural([1]))})  # 3
    result = poly1.MUL_PP_P(poly2)
    
    expected = Polynomial({
        0: Rational(Integer(0, Natural([3])), Natural([1])),   # + 3
        1: Rational(Integer(0, Natural([6])), Natural([1]))  # 6x
    })  # 6x + 3
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits

def test_mul_two_linear_polynomials():
    """Умножение двух линейных многочленов"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x
    })  # 2x + 1
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([4])), Natural([1])),   # + 4
        1: Rational(Integer(0, Natural([3])), Natural([1]))  # 3x
    })  # 3x + 4
    result = poly1.MUL_PP_P(poly2)
    
    # (2x + 1)(3x + 4) = 6x² + 8x + 3x + 4 = 6x² + 11x + 4
    expected = Polynomial({
        0: Rational(Integer(0, Natural([4])), Natural([1])),    # + 4
        1: Rational(Integer(0, Natural([1, 1])), Natural([1])),  # 11x
        2: Rational(Integer(0, Natural([6])), Natural([1]))   # 6x²
    })
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits

def test_mul_polynomials_different_degrees():
    """Умножение многочленов разных степеней"""
    poly1 = Polynomial({0: Rational(Integer(0, Natural([2])), Natural([1]))})  # 2
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([4])), Natural([1])),   # + 4
        1: Rational(Integer(0, Natural([3])), Natural([1]))  # 3x
    })  # 3x + 4
    result = poly1.MUL_PP_P(poly2)
    
    expected = Polynomial({
        0: Rational(Integer(0, Natural([8])), Natural([1])),   # + 8
        1: Rational(Integer(0, Natural([6])), Natural([1]))  # 6x
    })  # 6x + 8
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits

def test_mul_quadratic_with_linear():
    """Умножение квадратного многочлена на линейный"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x²
    })  # x² + 2x + 1
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([1])), Natural([1]))  # x
    })  # x + 1
    result = poly1.MUL_PP_P(poly2)
    
    # (x² + 2x + 1)(x + 1) = x³ + x² + 2x² + 2x + x + 1 = x³ + 3x² + 3x + 1
    expected = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x
        2: Rational(Integer(0, Natural([3])), Natural([1])),  # 3x²
        3: Rational(Integer(0, Natural([1])), Natural([1]))  # x³
    })
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits

def test_mul_with_only_highest_degree():
    """Умножение многочленов, где только старшие коэффициенты ненулевые"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1])),   # + 0
        1: Rational(Integer(0, Natural([2])), Natural([1]))  # 2x
    })  # 2x
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1])),   # + 0
        1: Rational(Integer(0, Natural([3])), Natural([1]))  # 3x
    })  # 3x
    result = poly1.MUL_PP_P(poly2)
    
    expected = Polynomial({
        0: Rational(Integer(0, Natural([0])), Natural([1])),  # + 0
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
        2: Rational(Integer(0, Natural([6])), Natural([1]))  # 6x²
    })  # 6x²
    # После валидации останется только 6x²
    assert result.m == 2
    assert result.coefficients[2].numerator.absolute.digits == [6]

def test_mul_complex_case():
    """Сложный случай умножения"""
    poly1 = Polynomial({
        0: Rational(Integer(0, Natural([2])), Natural([1])),   # + 2
        1: Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
        2: Rational(Integer(0, Natural([1])), Natural([1]))   # x²
    })  # x² + 2
    poly2 = Polynomial({
        0: Rational(Integer(0, Natural([1])), Natural([1])),   # + 1
        1: Rational(Integer(0, Natural([1])), Natural([1]))  # x
    })  # x + 1
    result = poly1.MUL_PP_P(poly2)
    
    # (x² + 2)(x + 1) = x³ + x² + 2x + 2
    expected = Polynomial({
        0: Rational(Integer(0, Natural([2])), Natural([1])),   # + 2
        1: Rational(Integer(0, Natural([2])), Natural([1])),  # 2x
        2: Rational(Integer(0, Natural([1])), Natural([1])),  # x²
        3: Rational(Integer(0, Natural([1])), Natural([1]))   # x³
    })
    
    assert len(result.coefficients) == len(expected.coefficients)
    for key in expected.coefficients.keys():
        assert result.coefficients[key].numerator.sign == expected.coefficients[key].numerator.sign
        assert result.coefficients[key].numerator.absolute.digits == expected.coefficients[key].numerator.absolute.digits
        assert result.coefficients[key].denominator.digits == expected.coefficients[key].denominator.digits
