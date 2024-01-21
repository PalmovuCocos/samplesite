"""
Данный модуль связывает проект с веб-сервером посредством интерфейса ASGI
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'samplesite.settings')

application = get_wsgi_application()
