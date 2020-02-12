from django.http import JsonResponse
from rice_server.settings import BASE_DIR
import json

import logging
logger = logging.getLogger('django')


def login(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
        return JsonResponse({
            'code': 20000,
            'data': "warehouseAdmin-token"
        })
    else:
        print(request.GET)
        return JsonResponse({})


def info(request):
    info = {
        'roles': ['admin'],
        'introduction': 'I am a super administrator',
        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        'name': 'Super Admin'
    }
    return JsonResponse({
        'code': 20000,
        'data': info
    })


def get_user_passwords(user):
    with open(BASE_DIR + "/config.json", encoding="utf-8") as f:
        data = json.load(f)
        return data[user]


def set_user_password(user, password):
    pass
