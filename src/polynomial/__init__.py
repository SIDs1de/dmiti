from .base_polynomial import BasePolynomial
from .mul_pq_p  import MUL_PQ_P

class Polynomial(
    BasePolynomial,
    MUL_PQ_P
):
    pass

__all__ = ['Polynomial']