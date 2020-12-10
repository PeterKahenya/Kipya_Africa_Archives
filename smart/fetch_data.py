import requests
import json


def get_token():
    url = "http://fliotex.faralenz.in:8080/api/auth/login"
    credentials = {
        "username": "info@adeptfluidyne.com",
        "password": "adept12!@"
    }

    headers={"Content-Type":"application/json"}

    response=requests.post(url,json=credentials,headers=headers)
    return json.loads(response.text)['token']


def get_reading():
    url="http://fliotex.faralenz.in:8080/api/plugins/telemetry/DEVICE/d7657500-932e-11e9-9fb0-057f71edcfec/values/timeseries?startTs=1581393196000&endTs=1582095728227"
    auth_token=get_token()
    # print(auth_token)
    headers={"Content-Type" : "application/json","X-Authorization":"Bearer "+auth_token}
    response=requests.get(url, headers=headers)
    print(json.loads(response.text))

get_reading()