from .base_rational import BaseRational
from .mul_qq_q  import MUL_QQ_Q
from .add_qq_q import ADD_QQ_Q
from .red_q_q import RED_Q_Q

class Rational(
    BaseRational,
    MUL_QQ_Q,
    ADD_QQ_Q,
    RED_Q_Q
):

    pass

__all__ = ['Rational']