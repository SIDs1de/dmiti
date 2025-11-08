from .base_integer import BaseInteger
from src.natural import Natural

class Trans_z_n:
	def trans_z_n(self: BaseInteger) -> Natural:
		"""
		Преобразование целого числа в натуральное.
		Если число отрицательное, выбрасывается ValueError.
		Если ноль, возвращает Natural([0]).
		"""
		if self.sign < 0:
			raise ValueError("Нельзя преобразовать отрицательное число в натуральное")
		# Возвращаем копию абсолютного значения
		return type(self.absolute)(self.absolute.digits.copy())