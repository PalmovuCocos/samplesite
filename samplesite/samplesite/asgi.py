"""
 модуль связывающий проект с веб-сервером через интерфейс ASGI
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'samplesite.settings')

application = get_asgi_application()
