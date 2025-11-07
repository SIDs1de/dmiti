from .base import BaseNatural

class ADD_1N_N:
<<<<<<< HEAD
	def ADD_1N_N(self: BaseNatural) -> BaseNatural:
		"""
		Добавление 1 к натуральному числу
		Автор: Дубровский Илья гр. 4383
		Возвращает новое натуральное число, равное self + 1
		"""
		digits = self.digits.copy()
		carry = 1  # перенос (начинаем с 1, т.к. прибавляем единицу)

		# Проходим по цифрам числа справа налево
		for i in range(len(digits) - 1, -1, -1):
			new_val = digits[i] + carry
			if new_val >= 10:
				digits[i] = new_val - 10
				carry = 1
			else:
				digits[i] = new_val
				carry = 0
				break

		# Если после всего цикла остался перенос — добавляем в начало
		if carry == 1:
			digits.insert(0, 1)

		return type(self)(digits)
=======
    def ADD_1N_N(self: BaseNatural) -> BaseNatural:
        """
        Добавление 1 к натуральному числу
        Автор: Дубровский Илья гр. 4383
        Возвращает новое натуральное число, равное self + 1
        """
        digits = self.digits.copy()
        carry = 1  # перенос (начинаем с 1, т.к. прибавляем единицу)

        # Проходим по цифрам числа справа налево
        for i in range(len(digits) - 1, -1, -1):
            new_val = digits[i] + carry
            if new_val >= 10:
                digits[i] = new_val - 10
                carry = 1
            else:
                digits[i] = new_val
                carry = 0
                break

        # Если после всего цикла остался перенос — добавляем в начало
        if carry == 1:
            digits.insert(0, 1)

        return type(self)(digits)
>>>>>>> 3402f02e852a977d2a15a05e2e73ab40545e4850
