from django.urls import path

from bboard.views import *
urlpatterns = [
    # name задаем для того, чтобы в шалонах можно было бы прописывать имена, вместо маршрутов
    # т.к. если поменяется utl у пути, то можно будет не менять их в шаблонах
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),  # параметризованный маршрут
    path('add/', BdCreateView.as_view(), name='add'),
]