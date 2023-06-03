import json
from mongoengine import connect
from get_model import Gets
from post_model import Posts
import requests
import os


connect(os.getenv("DB_NAME", "tests"), username=os.getenv("DB_USER", "root"), password=os.getenv("DB_PASSWORD",
        "root"), authentication_source='admin', host=os.getenv("DB_HOST", "localhost"), port=os.getenv("DB_PORT", 27017))
apiKey = 'ee867e313355e30237f283773f47ac1350bab3aa'
baseURL = 'https://api.appcenter.ms/v0.1'


def test_posts():
    print(chr(27) + '[1;37m\n' +
          '================================ Métodos POST ===============================')
    for test in Posts.objects:
        print(chr(27) + '[0;34m' + test._id + ' - ' + test.name)
        for data in test.data:
            print(chr(27) + '[0;33m\t' + data.name)
            resp = client_post(
                baseURL + test.endpoint.replace("{user_id}", data.request.uid), data.request.body)
            if (resp.status_code == data.expectedStatusCode):
                print(chr(27) + '[3;32m\tPass')
            else:
                print(chr(27) + '[3;31m\tNo Pass')
            assert resp.status_code == data.expectedStatusCode


def test_gets():
    print(chr(27) + '[1;37m\n' +
          '================================ Métodos GET ================================')
    for test in Gets.objects:
        print(chr(27) + '[0;34m' + test._id + ' - ' + test.name)
        for data in test.data:
            print(chr(27) + '[0;33m\t' + data.name)
            resp = client_get(
                baseURL + test.endpoint + add_parameters(data.request.params), data.request.headers)
            if (resp.status_code == data.expectedStatusCode):
                print(chr(27) + '[3;32m\tPass')
            else:
                print(chr(27) + '[3;31m\tNo Pass')
            assert resp.status_code == data.expectedStatusCode


def add_parameters(raw_params):
    if (len(raw_params) > 0 and raw_params[0].key == "no_key"):
        return raw_params[0].value
    return ""


def client_get(url: str, headers):
    resp = requests.get(url, headers=headers)
    return resp


def client_post(url: str, body):
    resp = requests.post(url, headers={
        "accept": 'application/json',
        'X-API-Token': apiKey,
        "Content-Type": "application/json"
    }, data=json.dumps(body))
    return resp


# def saveDevice():
#     payload = {'udid': '1',
#                'model': 'S20',
#                'os_build': '1',
#                'os_version': '12.2.5',
#                'serial': '',
#                'imei': '',
#                'owner_id': 'string'}
#     resp = save_device(
#         baseURL, 'f997d625-0bef-45b4-a5b3-e7cd43973fd6', {'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"}, payload)
#     formatResponse(resp, 'save device')


# def saveDeviceNoBody():
#     resp = save_device(
#         baseURL, 'f997d625-0bef-45b4-a5b3-e7cd43973fd6', {'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"})
#     formatResponse(resp, 'save device without payload')


# def saveDeviceNoUserId():
#     payload = {'udid': '1',
#                'model': 'S20',
#                'os_build': '1',
#                'os_version': '12.2.5',
#                'serial': '',
#                'imei': '',
#                'owner_id': 'string'}
#     resp = save_device(
#         baseURL, 'f997d625-0bef-45b4-e7cd43973fd6', {'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"}, payload)
#     formatResponse(resp, 'save device with wrong user id')

# def executeTest():
#     print(chr(27) + '[1;33m' + 'Get User')
#     userValidToken()
#     userInvalidToken()
#     userNotToken()
#     print(chr(27) + '[1;33m' + 'Save device')
#     saveDevice()
#     saveDeviceNoBody()
#     saveDeviceNoUserId()
#     print(chr(27) + '[1;33m' + 'Get device')
#     getDevice()
#     getDeviceNotFound()
#     getDeviceWrongToken()
#     print(chr(27) + '[1;33m' + 'Get devices')
#     getDevices()
#     getDevicesNotToken()
#     getDevicesInvalidToken()
#     print(chr(27) + '[1;33m' + 'Get devices')
#     deleteDevice()
#     deleteDeviceWrongId()
#     deleteDeviceNoToken()


# def deleteDevice():
#     resp = delete_device(baseURL, '1', {'accept': 'application/json',
#                                         "X-API-Token": apiKey, "Content-Type": "application/json"})
#     formatResponse(resp, 'delete device')


# def deleteDeviceWrongId():
#     resp = delete_device(baseURL, '3', {'accept': 'application/json',
#                                         "X-API-Token": apiKey, "Content-Type": "application/json"})
#     formatResponse(resp, 'delete dice with wrong id')


# def deleteDeviceNoToken():
#     resp = delete_device(baseURL, '1', {'accept': 'application/json',
#                                         "Content-Type": "application/json"})
#     formatResponse(resp, 'delete device')
