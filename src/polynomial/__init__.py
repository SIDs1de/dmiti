from .base_polynomial import BasePolynomial
from .mul_pq_p  import MUL_PQ_P
from .led_p_q  import LED_P_Q

class Polynomial(
    BasePolynomial,
    MUL_PQ_P,
    LED_P_Q
):
    pass

__all__ = ['Polynomial']