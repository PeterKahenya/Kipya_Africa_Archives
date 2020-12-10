from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Readings
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from boreholes.models import Payment,Borehole



class GetReadings(View):
    def get(self, request):
        meter_id = request.GET.get('meter_id')
        readings = Readings.objects.filter(meter=meter_id).order_by('time')
        readings_dict = []
        for reading in readings:
            readings_dict.append({
                "time": reading.time,
                "meter_id":reading.meter.id,
                "rate": reading.rate,
                "total": reading.total,
            })
        return JsonResponse(readings_dict, safe=False)


class PaymentsOptions(View):
    def get(self,request):
        return render(request,"payment_options.html",None,None)

@method_decorator(csrf_exempt, name='dispatch')
class LipaNaMPesa(View):
    def get(self,request):
        return render(request,"payment_option_mpesa.html",None,None)

    def post(self, request):
        borehole = Borehole.objects.all().filter(user=request.user).first()

        payment=Payment()
        payment.borehole=borehole
        payment.payment_method="MPESA"
        payment.user=request.user
        payment.code=request.POST.get('mpesa_code')
        payment.amount=request.POST.get('mpesa_amount')
        payment.account_no=request.POST.get('mpesa_name')
        payment.save()

        return redirect("/dashboard")
