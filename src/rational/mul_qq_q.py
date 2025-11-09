from src.integer import BaseInteger
from src.natural import BaseNatural
from src.rational import BaseRational

class MUL_QQ_Q:
    def MUL_QQ_Q(a: BaseRational, b: BaseRational) -> BaseRational:
        """
        Умножение двух рациональных чисел.
        Результат - рациональное число
        Автор: Рубан Егор гр.4383
        """

        numerator = a.numerator.mul_zz_z(b.numerator)

        denominator = a.denominator.MUL_NN_N(b.denominator)

        result = BaseRational(numerator, denominator)

        return result

