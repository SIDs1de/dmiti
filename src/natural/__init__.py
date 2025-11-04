from .base import Natural
from .com_nn_d import COM_NN_D

# Создаём финальный класс, наследуя от всех миксинов
class Natural(
    Natural,  # Базовый класс должен быть первым
    COM_NN_D
):
    """Полный класс натурального числа со всеми методами по ТЗ"""
    pass


# Экспортируем только финальный класс
__all__ = ['Natural']
