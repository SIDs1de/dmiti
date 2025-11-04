from .base_integer import Integer
from src.natural import Natural

class abs_z_n:
    """Абсолютная величина числа, результат - натуральное Z-1"""

    def abs_z_n(self: Integer) -> Natural:
        return self.absolute.copy()
