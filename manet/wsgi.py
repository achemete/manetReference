"""
WSGI config for manet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import 

#heroku 
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manet.settings")

application = get_wsgi_application()

#heroku
application = DjangoWhiteNoise(application)