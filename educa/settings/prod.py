from .base import *

DEBUG = False
ADMINS = (
    ('Ihfazh', 'me@ihfazh.com')
)

ALLOWED_HOSTS = ('ihfazh.com', 'www.ihfazh.com')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
        'HOST': 'localhost'
    }
}

