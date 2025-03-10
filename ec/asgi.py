"""
ASGI config for ec project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ec.settings")

# application = get_asgi_application()


from django.core.wsgi import get_wsgi_application
from asgiref.wsgi import WsgiToAsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ec.settings')
application = WsgiToAsgi(get_wsgi_application())

