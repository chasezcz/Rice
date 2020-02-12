from django.http import JsonResponse, HttpResponse
from rice_model.models import Worker

import json


def all(request):
    workersQS = Worker.objects.all()

    workers = workers_to_json(workersQS)
    return JsonResponse({
        'code': 20000,
        'data': workers
    })


def add(request):
    dataStr = request.GET.get('data')
    data = json.loads(dataStr)
    name = ''.join(data.get('name'))
    register_date = ''.join(data.get('register_date')[:10])
    last_work_date = ''.join(data.get('last_work_date')[:10])
    status = data.get('status')

    worker = Worker(
        name=name,
        register_date=register_date,
        last_work_date=last_work_date,
        status=status
    )
    worker.save()
    return JsonResponse({
        'code': 20000,
        'data': "success"
    })


# data: {"name":"wanggang","register_date":"2020-02-03T16:00:00.000Z","last_work_date":"2020-02-11T16:00:00.000Z","status":"ON"}
def workers_to_json(workers):
    list = []
    for worker in workers:
        list.append({
            'name': worker.name,
            'register_date': worker.register_date,
            'last_work_date': worker.last_work_date,
            'status': worker.status
        })
    return list
