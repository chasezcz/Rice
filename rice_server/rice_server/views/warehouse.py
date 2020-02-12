from django.http import JsonResponse, HttpResponse
from rice_model.models import Worker, Product
from . import worker, product
import json


def get_delivery_info(request):
    workersQS = Worker.objects.filter(status="ON")
    productsQS = Product.objects.exclude(status="OFF_SALE")
    workers = worker.workers_to_json(workersQS)
    products = product.products_to_json(productsQS)
    return JsonResponse({
        'code': 20000,
        'data': {
            'salers': workers,
            'products': products
        }
    })


def delivery(request):
    dataStr = request.GET.get('data')
    data = json.loads(dataStr)

    products = data.get('products')

    remarks = data.get('remarks')

    for product in products:
        label = product.get('label')
        number = int(product.get('number'))
        p = Product.objects.get(label=label)
        p.owned_number -= number
        p.save()

    return JsonResponse({
        'code': 20000,
        'data': "success"
    })


def collect(request):
    dataStr = request.GET.get('data')
    data = json.loads(dataStr)

    products = data.get('products')

    remarks = data.get('remarks')

    for product in products:
        label = product.get('label')
        number = int(product.get('number'))
        p = Product.objects.get(label=label)
        p.owned_number += number
        p.save()

    return JsonResponse({
        'code': 20000,
        'data': "success"
    })
