import requests
import base64
import json
from django.conf import settings
import os


def refresh_token():
    base_dir="media/helpers/"
    file = open(base_dir+'token.json', 'r+')
    tokens = json.loads(file.read())
    url = "https://zoom.us/oauth/token"
    print("Tokens"+str(tokens['refresh_token']))
    auth_credentials=base64.b64encode(b'aA1YAgUvTLi40U6CEGzPw:6yfPzT8xjvPxoaY6cPCfGCS3BubJ0b57')
    headers={
        "Authorization": "Basic "+str(auth_credentials,'utf-8')
    }
    data={
        "grant_type": "refresh_token",
        "refresh_token": tokens["refresh_token"]
    }
    file.close()
    file = open(base_dir+'token.json', 'w+')
    response=requests.post(url=url,data=data,headers=headers)
    print(response.text)
    file.write(response.text)
    file.close()
    return response.json()["access_token"]


    

def get_zoom_access_token():
    url="https://zoom.us/oauth/token"
    code="7ry0bqOZXu_IesK-rJvRAa3ajKVo6DTNg"
    data={
        "grant_type": 'authorization_code',
        "code": code,
        "redirect_uri": "https://www.eawaters.com/en/tokens"
    }
    auth_credentials=base64.b64encode(b'aA1YAgUvTLi40U6CEGzPw:6yfPzT8xjvPxoaY6cPCfGCS3BubJ0b57')
    headers={
        "Authorization": "Basic "+str(auth_credentials,'utf-8')
    }

    response=requests.post(url=url,data=data,headers=headers)

    file = open('media/helpers/token.json', 'w')
    file.write(response.text)
    file.close()
    print(response.text)
    return response.json()["access_token"]


def register(meeting_id,email,first_name,last_name):
    data='{"email":"'+email+'","first_name":"'+first_name+'","last_name":"'+last_name+'"}'
    print(data)
    access_token=refresh_token()

    headers={
        "Authorization":"Bearer "+access_token,
        "Content-Type":"application/json"
    }

    registration_url = "https://api.zoom.us/v2/meetings/"+meeting_id+"/registrants"
    response=requests.post(url=registration_url,json=json.loads(data),headers=headers)

    return response.json()["join_url"]

# register(meeting_id="91233382906",email="peter@kipya-africa.com",first_name="Peter",last_name="Kahenya")

get_zoom_access_token()

# refresh_token()