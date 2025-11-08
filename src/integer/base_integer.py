from src.natural import Natural


class BaseInteger:
    """Класс целого числа"""
    def __init__(self, sign: int, absolute: Natural):
        self.sign = sign # 0 - плюс, 1 - минус 
        self.absolute = absolute
        self._validate()

    def _validate(self):
        """Если число равно 0, то знак 0"""
        if len(self.absolute.digits) == 1 and self.absolute.digits[0] == 0:
            self.sign = 0

    def __str__(self):
        if self.iz_zero():
            return "0"
        elif self.sign == 1:
            return f"-{self.absolute}"
        else:
            return f"{self.absolute}"

    def __repr__(self):
        return f"Integer(sign={self.sign}, absolute={self.absolute})"

    def is_zero(self):
        """Проверка, что число равно нулю"""
        return (len(self.absolute.digits) == 1 and
                self.absolute.digits[0] == 0 and
                self.sign == 0)