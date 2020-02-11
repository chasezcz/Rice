from django.http import JsonResponse, HttpResponse
import logging


def user_login(request):
    if request.method == 'POST':

        logging.info(request)

        return JsonResponse({
            'code': 20000,
            'data': "warehouseAdmin-token"
        })


def user_info(request):
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


def get_delivery_info(request):
    return HttpResponse("yes")


def delivery(request):
    return HttpResponse()


def collect(request):
    return HttpResponse()
