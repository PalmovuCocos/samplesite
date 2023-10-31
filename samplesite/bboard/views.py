from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):

    '''
    :param request: это экземпляр класса HttpRequest
    он хранит различные сведения о полученом запросе: запрашиваемый интернет-адрес, данные клиента, служебную ин-ю и т д
    :return:
    '''

    s = 'Список объявлений'
    for bb in Bd.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'

    return HttpResponse(s, content_type='text/plain; charset=utf-8')
