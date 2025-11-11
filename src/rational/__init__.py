from .base_rational import BaseRational
from .mul_qq_q  import MUL_QQ_Q
from .int_q_b import INT_Q_B
from .add_qq_q import ADD_QQ_Q
from .sub_qq_q import SUB_QQ_Q
from .red_q_q import RED_Q_Q
from .trans_q_z import TRANS_Q_Z


class Rational(
    BaseRational,
    MUL_QQ_Q,
    INT_Q_B,
    ADD_QQ_Q,
    SUB_QQ_Q,
    RED_Q_Q,
    TRANS_Q_Z
):

    pass

__all__ = ['Rational']