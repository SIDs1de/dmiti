from src.natural import Natural


class Integer:
    """Базовый класс целого числа"""
    def __init__(self, sign: int, absolute: Natural):
        self.sign = sign
        self.absolute = absolute
        self._validate()

    def _validate(self):
        if len(self.absolute.digits) == 1 and self.absolute.digits[0] == 0:
            self.sign = 0

    def __str__(self):
        if self.sign == 0:
            return "0"
        return f"{'-' if self.sign < 0 else ''}{self.absolute}"

    def __repr__(self):
        return f"Integer(sign={self.sign}, absolute={self.absolute})"

    def is_zero(self):
        return self.sign == 0