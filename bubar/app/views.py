import logging
import json

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .form import gas_dp_form_clean, gas_qv_form_clean
from .steam_functions import get_flow_factor, cal_gas_dp, cal_gas_qv
from .models import log_history

logger = logging.getLogger("app")


@csrf_exempt
def handle_gas_dp(request):
    flow_type = 'gas'
    if request.method == "POST":
        logger.debug("cal dp {} ".format(flow_type))
        form_validate, params = gas_dp_form_clean(request.POST)
        if not form_validate:
            return HttpResponseBadRequest(params)

        flow_factor = get_flow_factor(flow_type, params['pipe_id'])
        dp1 = cal_gas_dp(
            params['tf'], params['mw'], params['flow_rate_c'], params['pb'],
            params['pf'], flow_factor, params['tb'], params['pipe_id'])

        dp2 = cal_gas_dp(
            params['tf'], params['mw'], params['flow_rate_c'], params['pb'],
            params['pf'], flow_factor, params['tb'], params['pipe_id'])

        l = log_history(flow_type, params['project_name'], params['operator'], params)
        return HttpResponse(json.dumps(
            {"dp1": dp1, "dp2": dp2, "pipe_id": params['pipe_id'],
             "time": timezone.localtime(l.create_time).strftime("%Y-%m-%d %H:%M")}
        ))
    else:
        return render(request, 'gas.html', {})


@csrf_exempt
def handle_gas_qv(request):
    flow_type = 'gas'
    if request.method == "POST":
        logger.debug("cal qv {} ".format(flow_type))
        form_validate, params = gas_qv_form_clean(request.POST)
        if not form_validate:
            return HttpResponseBadRequest(params)

        flow_factor = get_flow_factor(flow_type, params['pipe_id'])
        qv = cal_gas_qv(
            params['tf'], params['mw'], params['flow_rate_c'], params['pb'],
            params['pf'], flow_factor, params['tb'], params['pipe_id'])

        # l = log_history(flow_type, params['project_name'], params['operator'], params)
        return HttpResponse(json.dumps({"qv": qv}))
    else:
        return HttpResponse({})


@csrf_exempt
def cal_liquid(request):
    return render(request, 'liquid.html', {})


@csrf_exempt
def cal_steam(request):
    return render(request, 'steam.html', {})

@csrf_exempt
def test(request):
    return render(request, 'test.html', {})
