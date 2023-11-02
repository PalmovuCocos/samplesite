from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import BdForm
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


class BdCreateView(CreateView):
    template_name = 'bboard/create.html'    # путь к файлу шаблона
    form_class = BdForm         # ссылка на класс формы, связанной с моделью
    # данная функция принимает имя маршрута и результатом становится готовый интернет-адрес
    success_url = reverse_lazy('index')    # на какой адрес перенаправлять после успешного сохранения данных

    # данный метод формирует контекст шаблона
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
