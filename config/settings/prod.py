from pathlib import Path
from decouple import config,Csv
from .base import *

DEBUG = config("DEBUG", cast = bool, default = True)
ALLOWED_HOSTS += ["127.0.0.1","localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lmsdb',
        'USER': 'postgres',
        'PASSWORD' : '1190',
        'HOST' : 'localhost',
        'PORT' : '5433',
    }
}

 