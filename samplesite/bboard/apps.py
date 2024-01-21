'''
Модуль с настройками приложения
'''
from django.apps import AppConfig


class BboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bboard'    # полный путь к пакету приложения относительно папки проекта
    label = 'bboard'    # псевдоним приложения
    verbose_name = 'Доска объявлений'   # данное название будет отображаться в admin'ке сайта
