from src.integer import Integer
from src.natural import Natural
from src.rational import Rational
from src.polynomial import Polynomial

p1 = Polynomial({
    5: Rational(Integer(0, Natural([2])), Natural([3])),
    0: Rational(Integer(0, Natural([1])), Natural([1])),
})

p2 = Polynomial({
    5: Rational(Integer(0, Natural([2])), Natural([6])),
    2: Rational(Integer(1, Natural([2])), Natural([1])),
})


print(p1)
