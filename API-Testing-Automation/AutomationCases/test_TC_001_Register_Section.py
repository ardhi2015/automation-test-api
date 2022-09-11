import requests
import json
import jsonpath
import random
from random_phone_generator import *



baseUrl = "http://pretest-qa.dcidev.id/"
phone_number = random_phone_num_generator()


# Register dengan nomor baru
def test_successful_registration() :
    path = "api/v1/register"
    data = {
        "phone": "627821219292",
        "password": "testing",
        "country": "Indonesia",
        "latlong": "23232032",
        "device_token": "1",
        "device_type" : 1
    }

    data["phone"] = phone_number

    url=baseUrl+path

    response = requests.post(url, json=data)
    assert response.status_code == 201
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())
 
# Register dengan nomor yang sudah terdaftar
def test_registration_using_registered_number() :
    path = "api/v1/register"
    data = {
        "phone": "627821219292",
        "password": "testing",
        "country": "Indonesia",
        "latlong": "23232032",
        "device_token": "1",
        "device_type" : 1
    }

    data["phone"] = phone_number

    url=baseUrl+path

    response = requests.post(url, json=data)
    assert response.status_code == 422
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())



def test_remove_registered_number() :
    path = "api/v1/register/remove"
    data = {
        "phone": "627821219292"
    }
    data["phone"] = phone_number
    url=baseUrl+path

    response = requests.post(url, json=data)
    assert response.status_code == 201
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())




