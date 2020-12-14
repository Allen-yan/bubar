import math

from .models import Factor


def get_flow_factor(flow_type, pipe_inner_diameter):
    """

    :param flow_type:
    :param pipe_inner_diameter: 管道内径
    :return:
    """
    f = Factor.objects.filter(
        flow_type=flow_type, pipe_id_max__lt=pipe_inner_diameter, pipe_id_min__gte=pipe_inner_diameter)
    if len(f) > 2:
        raise
    return f.first().factor


def cal_gas_dp(tf, mw, qv, pb, pf, f, tb, d):
    tfa = tf + 273.15
    tba = tb + 273.15
    pfa = pf + 101.32

    return tfa * mw * math.pow(qv, 2) * math.pow(pb, 2) \
           / (pfa * math.pow(f, 2) * math.pow(tba, 2) * math.pow(d, 4))
