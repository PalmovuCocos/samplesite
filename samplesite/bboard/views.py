from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    '''
    :param request: это экземпляр класса HttpRequest
    он хранит различные сведения о полученом запросе: запрашиваемый интернет-адрес, данные клиента, служебную ин-ю и т д
    :return:
    '''
    # загрузка шаблона (возвращает объект класса Template)
    template = loader.get_template('bboard/index.html')
    # взятие всех записей
    bbs = Bd.objects.order_by('-published')
    # формирование словаря content для передачи в httpResponse
    content = {'bbs': bbs}
    # выполнение рендеринга шаблона с помощью метода render
    # в итоне в httpResponse поступает html строка
    return HttpResponse(template.render(content, request))
