import dj_database_url

from base import *


DATABASES['default'] =  dj_database_url.config()

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']


# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]
