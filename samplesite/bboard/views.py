from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import *


def index(request):
    '''
    :param request: это экземпляр класса HttpRequest
    он хранит различные сведения о полученом запросе: запрашиваемый интернет-адрес, данные клиента, служебную ин-ю и т д
    :return:
    '''
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    content = {'bbs': bbs, 'rubrics': rubrics}

    return render(request, 'bboard/index.html', content)


def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    content = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', content)

