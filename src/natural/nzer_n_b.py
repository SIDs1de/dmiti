from .base import BaseNatural

class NZER_N_B:
    def NZER_N_B(self: BaseNatural) -> str:
        """
        Проверка на ноль
        Автор: Королев Семен гр. 4382
        Возвращает:
        "да" - если число не равно 0
        "нет" - если число равно 0
        """

        if len(self.digits) == 1 and self.digits[0] == 0:
            return "нет"
        else:
            return "да"