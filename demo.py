from src.integer import Integer
from src.natural import Natural
from src.rational import Rational
from src.polynomial import Polynomial

print("=== ДЕМОНСТРАЦИЯ РАБОТЫ FAC_P_Q ===")

# --- Пример 1: Полином с целыми коэффициентами ---
print("\nПример 1: Целые коэффициенты")
coeffs1 = [
    Rational(Integer(0, Natural([6])), Natural([1])),  # 6x^2
    Rational(Integer(0, Natural([9])), Natural([1])),  # 9x
    Rational(Integer(0, Natural([3])), Natural([1]))   # 3
]
poly1 = Polynomial(coeffs1)
print("Полином:", [str(c) for c in poly1.coefficients])
factor1 = poly1.FAC_P_Q()
print("FAC_P_Q:", factor1) # Ожидаем: 3/1 (НОД(6,9,3)=3, НОК(1,1,1)=1)

# --- Пример 2: Полином с дробными коэффициентами ---
print("\nПример 2: Дробные коэффициенты")
coeffs2 = [
    Rational(Integer(0, Natural([4])), Natural([6])),   # (4/6)x^2
    Rational(Integer(0, Natural([8])), Natural([1,2])),  # (8/12)x
    Rational(Integer(0, Natural([2])), Natural([3]))    # (2/3)
]
poly2 = Polynomial(coeffs2)
print("Полином:", [str(c) for c in poly2.coefficients])
factor2 = poly2.FAC_P_Q()
print("FAC_P_Q:", factor2) # Ожидаем: 2/12 -> 1/6 (НОД(4,8,2)=2, НОК(6,12,3)=12)

# --- Пример 3: Полином с нулевым коэффициентом ---
print("\nПример 3: С нулевым коэффициентом")
coeffs3 = [
    Rational(Integer(0, Natural([6])), Natural([1])),  # 6x^2
    Rational(Integer(0, Natural([0])), Natural([1])),  # 0x
    Rational(Integer(0, Natural([3])), Natural([1]))   # 3
]
poly3 = Polynomial(coeffs3)
print("Полином:", [str(c) for c in poly3.coefficients])
factor3 = poly3.FAC_P_Q()
print("FAC_P_Q:", factor3) # Ожидаем: 3/1 (НОД(6,3)=3, НОК(1,1,1)=1, 0 игнорируется)

# --- Пример 4: Нулевой полином ---
print("\nПример 4: Нулевой полином")
coeffs4 = [
    Rational(Integer(0, Natural([0])), Natural([1])),
    Rational(Integer(0, Natural([0])), Natural([1])),
    Rational(Integer(0, Natural([0])), Natural([1]))
]
poly4 = Polynomial(coeffs4)
print("Полином:", [str(c) for c in poly4.coefficients])
factor4 = poly4.FAC_P_Q()
print("FAC_P_Q:", factor4) # Ожидаем: 1/1 (по условию для нулевого полинома)

# --- Пример 5: Полином с отрицательными коэффициентами ---
print("\nПример 5: С отрицательными коэффициентами")
coeffs5 = [
    Rational(Integer(1, Natural([1,2])), Natural([1])),  # -12x^2
    Rational(Integer(0, Natural([1,8])), Natural([1])),  # 18x
    Rational(Integer(1, Natural([6])), Natural([1]))    # -6
]
poly5 = Polynomial(coeffs5)
print("Полином:", [str(c) for c in poly5.coefficients])
factor5 = poly5.FAC_P_Q()
print("FAC_P_Q:", factor5) # Ожидаем: 6/1 (НОД(|-12|,|18|,|-6|)=НОД(12,18,6)=6, НОК(1,1,1)=1)

print("\n=== ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА ===")
