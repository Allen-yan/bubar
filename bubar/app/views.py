import logging
import json

from django.utils.safestring import SafeString

from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core import serializers


from .form import gas_dp_form_clean, gas_qv_form_clean, serializer_history_operation, \
    liquid_dp_form_clean, liquid_qm_form_clean
from .steam_functions import get_flow_factor, cal_gas_dp, cal_gas_qv, cal_liquid_dp, cal_liquid_qm
from .models import log_history, OperationHistory

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
            params['tf'], params['mw'], params['flow_rate_min'], params['pb'],
            params['pf'], flow_factor, params['tb'], params['pipe_id'])

        l = log_history(
            flow_type, params['project_name'], params['operator'], params,
            {'dp1': dp1, 'dp2': dp2}, flow_factor
        )
        return HttpResponse(json.dumps({"id": l.id}))
        # return HttpResponse(json.dumps(
        #     {"dp1": dp1, "dp2": dp2, "pipe_id": params['pipe_id'],
        #      "time": timezone.localtime(l.create_time).strftime("%Y-%m-%d %H:%M")}
        # ))
        # return redirect("/bubar/gas?id={}".format(l.id))
    else:
        data = {}
        if 'id' in request.GET:
            ph = OperationHistory.objects.filter(id=request.GET['id']).first()
            data = serializer_history_operation(ph) if ph else {}
        logger.debug(data)
        data['data'] = SafeString(data)
        return render(request, 'gas.html', data)


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
            params['tf'], params['mw'], params['dp'], params['pb'],
            params['pf'], float(flow_factor), params['tb'], params['pipe_id'])

        # l = log_history(flow_type, params['project_name'], params['operator'], params)
        return HttpResponse(json.dumps({"qv": qv}))
    else:
        return HttpResponse({})


@csrf_exempt
def handle_liquid_dp(request):
    flow_type = 'liquid'
    if request.method == "POST":
        logger.debug("cal dp {} ".format(flow_type))
        form_validate, params = liquid_dp_form_clean(request.POST)
        if not form_validate:
            return HttpResponseBadRequest(params)

        flow_factor = get_flow_factor(flow_type, params['pipe_id'])
        dp1 = cal_liquid_dp(params['flow_rate_c'], params['gf'], flow_factor, params['pipe_id'])

        dp2 = cal_liquid_dp(params['flow_rate_min'], params['gf'], flow_factor, params['pipe_id'])

        l = log_history(
            flow_type, params['project_name'], params['operator'], params,
            {'dp1': dp1, 'dp2': dp2}, flow_factor
        )
        return HttpResponse(json.dumps({"id": l.id}))
    else:
        data = {}
        if 'id' in request.GET:
            ph = OperationHistory.objects.filter(id=request.GET['id']).first()
            data = serializer_history_operation(ph) if ph else {}
        logger.debug(data)
        data['data'] = SafeString(data)
        return render(request, 'liquid.html', data)


@csrf_exempt
def handle_liquid_qm(request):
    flow_type = 'liquid'
    if request.method == "POST":
        logger.debug("cal qm {} ".format(flow_type))
        form_validate, params = liquid_qm_form_clean(request.POST)
        if not form_validate:
            return HttpResponseBadRequest(params)

        flow_factor = get_flow_factor(flow_type, params['pipe_id'])
        qm = cal_liquid_qm(float(flow_factor), params['pipe_id'],  params['gf'], params['dp'])

        # l = log_history(flow_type, params['project_name'], params['operator'], params)
        return HttpResponse(json.dumps({"qm": qm}))
    else:
        return HttpResponse({})


@csrf_exempt
def cal_steam(request):
    return render(request, 'steam.html', {})

@csrf_exempt
def test(request):
    return render(request, 'test.html', {})
