from .base_polynomial import BasePolynomial
from .mul_pq_p  import MUL_PQ_P
from .led_p_q  import LED_P_Q
from .deg_p_n import DEG_P_N
from .sub_pp_p import SUB_PP_P
from .mul_pxk_p import MUL_Pxk_P


class Polynomial(
    BasePolynomial,
    MUL_PQ_P,
    LED_P_Q,
    DEG_P_N,
    SUB_PP_P,
    MUL_Pxk_P
):
    pass

__all__ = ['Polynomial']