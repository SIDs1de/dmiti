from .base import BaseNatural
from .com_nn_d import COM_NN_D
from .mul_nd_n import MUL_ND_N 
from .mul_nk_n import MUL_Nk_N 
from .mul_nn_n import MUL_NN_N
from .nzer_n_b import NZER_N_B
from .add_1n_n import ADD_1N_N
from .add_nn_n import ADD_NN_N
from .div_nn_dk import DIV_NN_DK
from .sub_nn_n import SUB_NN_N
from .div_nn_n import DIV_NN_N


class Natural(
	BaseNatural,
	COM_NN_D,
	MUL_ND_N,
	MUL_Nk_N,
	MUL_NN_N,
	NZER_N_B,
	ADD_1N_N,
	ADD_NN_N,
	DIV_NN_DK,
	SUB_NN_N,
	DIV_NN_N
):
	"""Класс натурального числа"""
	pass

__all__ = ['Natural']