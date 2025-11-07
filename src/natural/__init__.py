from .base import BaseNatural
from .com_nn_d import COM_NN_D
from .mul_nd_n import MUL_ND_N 
from .mul_nk_n import MUL_Nk_N 
from .nzer_n_b import NZER_N_B
from .add_1n_n import ADD_1N_N

class Natural(
	BaseNatural,
	COM_NN_D,
	MUL_ND_N,
	MUL_Nk_N,
	NZER_N_B,
	ADD_1N_N
):
	"""Класс натурального числа"""
	pass

# Экспортируем только финальный класс
__all__ = ['Natural']
