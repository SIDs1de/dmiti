from .base_rational import BaseRational
from .mul_qq_q  import MUL_QQ_Q
from .add_qq_q import ADD_QQ_Q

class Rational(
    BaseRational,
    MUL_QQ_Q,
    ADD_QQ_Q
):

    pass

__all__ = ['Rational']