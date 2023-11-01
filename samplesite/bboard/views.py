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
    bbs = Bd.objects.order_by('-published')

    return render(request, 'bboard/index.html', {'bbs': bbs})
