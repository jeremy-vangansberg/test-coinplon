"""
ASGI config for coinplon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from coinplon.settings import base


if base.DEBUG :
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinplon.settings.dev')
else : 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinplon.settings.prod')

application = get_asgi_application()
