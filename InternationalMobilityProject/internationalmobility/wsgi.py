"""
WSGI config for internationalmobility project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Changement à faire par rapport à la mise en production du site
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internationalmobility.settings.development')

application = get_wsgi_application()
