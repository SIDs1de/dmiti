from .base import Natural
from .comparison import NaturalComparison
from .arithmetic import NaturalArithmetic
from .multiplication import NaturalMultiplication
from .division import NaturalDivision
from .gcd_lcm import NaturalGCDLCM


# Создаём финальный класс, наследуя от всех миксинов
class Natural(
    Natural,  # Базовый класс должен быть первым
    NaturalComparison,
    NaturalArithmetic,
    NaturalMultiplication,
    NaturalDivision,
    NaturalGCDLCM
):
    """Полный класс натурального числа со всеми методами по ТЗ"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']
