import math

from .models import Factor
from . import sqls
from .utils import db_fetch_one


def get_flow_factor(flow_type, pipe_inner_diameter):
    """

    :param flow_type:
    :param pipe_inner_diameter: 管道内径
    :return:
    """
    f_max = db_fetch_one(sqls.max_factor.format(flow_type))
    f_min = db_fetch_one(sqls.min_factor.format(flow_type))

    if pipe_inner_diameter >= f_max:
        f = Factor.objects.filter(flow_type=flow_type, pipe_id_max=f_max)
    elif pipe_inner_diameter < f_min:
        f = Factor.objects.filter(flow_type=flow_type, pipe_id_min=f_min)
    else:
        f = Factor.objects.filter(
            flow_type=flow_type, pipe_id_max__gte=pipe_inner_diameter, pipe_id_min__lte=pipe_inner_diameter)
    if not f or len(f) >= 2:
        raise ValueError("Failed to find factor for {}, {}".format(flow_type, pipe_inner_diameter))
    return f.first().factor


def cal_gas_dp(tf, mw, c, pb, pf, f, tb, d):
    tfa = tf + 273.15
    tba = tb + 273.15
    pfa = pf + 101.32

    return tfa * mw * math.pow(c, 2) * math.pow(pb, 2) \
           / (pfa * math.pow(f, 2) * math.pow(tba, 2) * math.pow(d, 4))


def cal_gas_qv(tf, mw, dp, pb, pf, f, tb, d):
    tfa = tf + 273.15
    tba = tb + 273.15
    pfa = pf + 101.32

    tmp = math.sqrt(dp * pfa / (mw * tfa))
    return f * math.pow(d, 2) * tba * tmp / pb


def cal_liquid_dp(qm, gf, f, d):
    return math.pow(qm, 2) / (gf * math.pow(f, 2) * math.pow(d, 4))


def cal_liquid_qm(f, d, gf, dp):
    tmp = math.sqrt(gf * dp)
    return f * math.pow(d, 2) * tmp


def cal_steam_dp(qm, od, f, d):
    return math.pow(qm, 2) / (od * math.pow(f, 2) * math.pow(d, 4))


def cal_steam_qm(f, d, od, dp):
    tmp = math.sqrt(od * dp)
    return f * math.pow(d, 2) * tmp
