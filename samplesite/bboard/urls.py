from django.urls import path

from bboard.views import index, by_rubric

urlpatterns = [
    path('', index),
    path('<int:rubric_id>/', by_rubric) # параметризованный маршрут
]