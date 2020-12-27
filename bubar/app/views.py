import logging
import json

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from .steam_functions import get_flow_factor, cal_gas_dp

logger = logging.getLogger("app")


def gas_form_clean(payload):
    form_validator = {  # key: (type, required)
        'pipe_id': (float, True),
        'pf': (float, True),
        'tf': (float, True),
        'flow_rate_min': (float, False),
        'flow_rate_nor': (float, False),
        'flow_rate_max': (float, False),
        'flow_rate_c': (float, True),
        'mw': (float, True),
        'tb': (float, True),
        'pb': (float, True),

        'project_name': (str, True),
        'operator': (str, True),
        'page': (str, True),
        'fluid_name': (str, True),
        'tag_number': (str, True),
        'pipe_od': (str, True),
        'pipe_material': (str, True),
        'pipe_direction': (str, True),
        'press_rating': (str, True),
        'pipe_orientation': (str, True),
        'dp_conn_type': (str, True),

    }
    result = {}
    for f, (f_type, f_required) in form_validator.items():
        logger.debug("validate field {}, {}, {}".format(f, f_type, f_required))
        if f in payload:
            try:
                result[f] = f_type(payload[f])
            except ValueError:
                return False, "{} require {}!".format(f, str(f_type))
        else:
            if f_required:
                return False, "{} required".format(f)

    return True, result


@csrf_exempt
def cal_gas(request):
    if request.method == "POST":
        form_validate, params = gas_form_clean(request.POST)
        if not form_validate:
            return HttpResponseBadRequest(params)

        flow_factor = get_flow_factor('gas', params['pipe_id'])
        dp1 = cal_gas_dp(
            params['tf'], params['mw'], params['flow_rate_c'], params['pb'],
            params['pf'], flow_factor, params['tb'], params['pipe_id'])

        dp2 = cal_gas_dp(
            params['tf'], params['mw'], params['flow_rate_c'], params['pb'],
            params['pf'], flow_factor, params['tb'], params['pipe_id'])

        return HttpResponse(json.dumps({"dp1": dp1, "dp2": dp2, "pipe_id": params['pipe_id'], "time": ""}))
    else:
        return render(request, 'gas.html', {})


@csrf_exempt
def cal_liquid(request):
    return render(request, 'liquid.html', {})


@csrf_exempt
def cal_steam(request):
    return render(request, 'steam.html', {})

@csrf_exempt
def test(request):
    return render(request, 'test.html', {})
