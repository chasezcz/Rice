from django.http import HttpResponse


def get_delivery_info(request):
    return HttpResponse("yes")


def delivery(request):
    return HttpResponse()


def collect(request):
    return HttpResponse()
