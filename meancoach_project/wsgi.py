"""
WSGI config for meancoach project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', None)
assert settings_module, "DJANGO_SETTINGS_MODULE environment variable not set"

application = Cling(get_wsgi_application())
