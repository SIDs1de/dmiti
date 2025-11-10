from .base_rational import BaseRational
from .mul_qq_q  import MUL_QQ_Q
from .int_q_b import INT_Q_B


class Rational(
    BaseRational,
    MUL_QQ_Q,
    INT_Q_B
):

    pass

__all__ = ['Rational']