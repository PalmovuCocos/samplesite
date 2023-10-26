from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    '''
    :param request: это экземпляр класса HttpRequest
    он хранит различные сведения о полученом запросе: запрашиваемый интернет-адрес, данные клиента, служебную ин-ю и т д
    :return:
    '''

    return HttpResponse("Здесь будет выведен список объявлений.")
