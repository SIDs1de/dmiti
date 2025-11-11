from typing import Self
from src.rational import Rational


class LED_P_Q:
    def LED_P_Q(self: Self) -> Rational:
        """
        Возвращает старший коэффициент многочлена
        Автор: Королев Семен гр. 4382
        """
        return self.coefficients[0]