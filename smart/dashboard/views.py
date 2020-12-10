from django.shortcuts import render
from django.views import View
from boreholes.models import Borehole
from readings.models import Readings
import requests
import json
from datetime import datetime
import threading
from django.db.models import Max



class DashboardView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.borehole = None
        threading.Timer(1.0, self.get_reading).start()

    def get_token(self):
        url = "http://fliotex.faralenz.in:8080/api/auth/login"
        credentials = {
            "username": "info@adeptfluidyne.com",
            "password": "adept12!@"
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=credentials, headers=headers)
        return json.loads(response.text)['token']

    def get_reading(self):
        startTs = int(datetime.strptime('Mar 1 2020  1:33PM', '%b %d %Y %I:%M%p').timestamp() * 1000)
        endTs = int(datetime.now().timestamp() * 1000)

        # url = "http://fliotex.faralenz.in:8080/api/plugins/telemetry/DEVICE/"+borehole.meter.device_id+"/values/timeseries?startTs="\
        #       +str(startTs)+"&endTs="+str(endTs)+"&limit=100"
        url = "http://fliotex.faralenz.in:8080/api/plugins/telemetry/DEVICE/d7657500-932e-11e9-9fb0-057f71edcfec/values/timeseries?startTs=" \
              + str(startTs) + "&endTs=" + str(endTs) + "&limit=100"

        auth_token = self.get_token()
        headers = {"Content-Type": "application/json", "X-Authorization": "Bearer " + auth_token}
        response_json = json.loads(requests.get(url, headers=headers).text)
        print(response_json['S1R1'])
        print(response_json['S1R2'])

        last_reading_time = Readings.objects.filter(meter=self.borehole.meter).aggregate(Max("time"))['time__max']
        if last_reading_time is None or last_reading_time < response_json['S1R1'][0]['ts']:
            r = Readings()
            r.meter = self.borehole.meter
            r.time= int(response_json['S1R1'][0]['ts'])
            r.rate= response_json['S1R1'][0]['value']
            r.total=response_json['S1R2'][0]['value']
            r.save()
            print("New Reading")


        print(last_reading_time)
        # print(Readings.objects.aggregate(self.borehole.meter)

        threading.Timer(1.0, self.get_reading).start()

    def get(self, request):
        self.borehole = Borehole.objects.all().filter(user=request.user).first()
        return render(request, "dashboard.html", {'borehole': self.borehole})

class WRAView(View):
    def get(self,request):
        return render(request,"mapview.html",None,None)
    def post(self,request):
        pass

class WRABoreholeDashboard(View):
    def get(self,request):
        return render(request,"wra_dashboard.html",None,None)