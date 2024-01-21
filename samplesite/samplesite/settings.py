
from pathlib import Path

# путь к папке проекта
BASE_DIR = Path(__file__).resolve().parent.parent



# секретный ключ для шифрования важных данных
SECRET_KEY = 'django-insecure-etw7w9-btv))37vh4z(omjr0ae+9(hg9rix!ii13h9c#&_2sj@'

# режим работы сайта (отладочный или нет)
DEBUG = True

ALLOWED_HOSTS = []

# список зарегестрированных приложений
INSTALLED_APPS = [
    'django.contrib.admin',    # административный сайт Django
    'django.contrib.auth',  # подсистема разграничения доступа
    'django.contrib.contenttypes',    # хранит список всех моделей из всех приложений сайта
    'django.contrib.sessions',    # подсистема обслуживающая серверные сессии
    'django.contrib.messages',  # выводит всплывающие сообщения
    'django.contrib.staticfiles',   # обрабатыват статические файлы
    'bboard',    # подключение приложения bboard (заходит в __init__ и там ищет путь)
]

# модуль для предварительной обработки клиентского запроса перед передачей его контроллеру
# и окончательной обработки ответа сгенерированного контроллером
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',    # доп защита от сетевых атак.
    'django.contrib.sessions.middleware.SessionMiddleware',    #
    'django.middleware.common.CommonMiddleware',    # учавствует в предварительной обработке запроса
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'samplesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'samplesite.wsgi.application'


# запись данных о используемой балзе данных
DATABASES = {
    # 'default это псевдоним данной БД'
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',    # формат используемой бд
        'NAME': BASE_DIR / 'db.sqlite3',    # путь к файлу БД
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# язык языка для системных сообщений и страниц администратора сайта
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
