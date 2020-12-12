from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cal_gas(request):

    return render(request, 'gas.html', {})
