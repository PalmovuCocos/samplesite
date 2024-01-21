from django.contrib import admin
from django.urls import path, include

from bboard.views import index
urlpatterns = [
    # Когда джанго находит bboard, то удаляет его и переходим к bboard.urls (надо разобраться что делает include)
    path('bboard/', include('bboard.urls')), # добавляем вложеный список маршрутов вторым аргументом
    path('admin/', admin.site.urls),
]
