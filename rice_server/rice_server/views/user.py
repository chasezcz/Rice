from django.http import JsonResponse
from rice_server.settings import admin_tokens, warehouseAdmin_tokens
from rice_server.settings import BASE_DIR
import json
from random import Random
import logging
logger = logging.getLogger('django')


def login(request):
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
        return JsonResponse({
            'code': 500,
            'data': ''
        })
    else:
        dataStr = request.GET.get('data')
        data = json.loads(dataStr)
        username = data.get('username')
        password = data.get('password')

        valid_usernames = ["admin", "warehouseAdmin"]

        err = ""

        if username in valid_usernames:

            valid_password = get_user_passwords(username)
            if password == valid_password:
                return JsonResponse({
                    'code': 20000,
                    'data': {
                        'token': get_random_token(username),
                    }
                })
            else:
                err = "密码不正确"
        else:
            err = "用户名不正确"
        return JsonResponse({
            'code': "500",
            'data': err
        })


def info(request):
    token = request.GET.get('token')
    if token in admin_tokens:
        info = {
            'roles': ['admin'],
            'introduction': 'I am a super administrator',
            'avatar': '',
            'name': 'Super Admin'
        }
        return JsonResponse({
            'code': 20000,
            'data': info
        })
    elif token in warehouseAdmin_tokens:
        info = {
            'roles': ['warehouseAdmin'],
            'introduction': '仓库管理员',
            'avatar': '',
            'name': '仓库管理员'
        }
        return JsonResponse({
            'code': 20000,
            'data': info
        })
    else:
        return JsonResponse({
            'code': 50008,
            'message': "登录失败，token无效"
        })


def logout(request):
    return JsonResponse({
        'code': 20000,
        'data': '成功'
    })


def get_user_passwords(user):
    with open(BASE_DIR + "/config.json", encoding="utf-8") as f:
        data = json.load(f)
        return data['passwords'][user]


def set_user_password(user, password):
    pass


def get_random_token(username):
    if username == 'admin':
        random_token = get_token()
        while random_token in admin_tokens:
            random_token = get_token
        admin_tokens.append(random_token)
        return random_token
    else:
        random_token = get_token()
        warehouseAdmin_tokens.append(random_token)
        return random_token


def get_token():
    length_r = 32
    token = ''
    chars = 'qwertyuiopoasdfghjklzxcvbnm0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(length_r):
        token += chars[random.randint(0, length)]
    return token
