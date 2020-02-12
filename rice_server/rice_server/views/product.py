from django.http import JsonResponse, HttpResponse
from rice_model.models import Product

import json


def all(request):
    productsQS = Product.objects.all()

    products = products_to_json(productsQS)
    print(products)
    return JsonResponse({
        'code': 20000,
        'data': products
    })


def add(request):
    dataStr = request.GET.get('data')
    data = json.loads(dataStr)

    label = ''.join(data.get('label'))
    last_supple_date = ''.join(data.get('last_supple_date')[:10])
    status = data.get('status')
    owned_number =  int(''.join(data.get('owned_number')))

    product = Product(
        label=label,
        last_supple_date=last_supple_date,
        owned_number=owned_number,
        status=status
    )
    product.save()
    return JsonResponse({
        'code': 20000,
        'data': "success"
    })


def products_to_json(products):
    list = []
    for product in products:
        list.append({
            'label': product.label,
            'owned_number': product.owned_number,
            'last_supple_date': product.last_supple_date,
            'status': product.status
        })
    return list
