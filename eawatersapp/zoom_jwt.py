import requests
import base64
import json
import os

jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaXNzIjoiaVVEVm1sY3ZUdUNLajAtME9Ib1RqdyIsImV4cCI6MTY0MDkwODgwMH0.uViR5DEs1w_qet-y-r7l-gFdzkzu40mzyJ3HF-GiSdk"
def get_users():

    url = "https://api.zoom.us/v2/users"

    headers={
        "Authorization": "Bearer "+jwt
    }
    response=requests.get(url=url,headers=headers)
    print(response.text)

def register(meeting_id,email,first_name,last_name):
    data='{"email":"'+email+'","first_name":"'+first_name+'","last_name":"'+last_name+'"}'

    headers={
        "Authorization":"Bearer "+jwt,
        "Content-Type":"application/json"
    }

    registration_url = "https://api.zoom.us/v2/meetings/"+meeting_id+"/registrants"
    response=requests.post(url=registration_url,json=json.loads(data),headers=headers)
    return response.json()["join_url"]

register(meeting_id="91233382906",email="peter@kipya-africa.com",first_name="Peter",last_name="Kahenya")

# get_users()



  