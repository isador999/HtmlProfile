"""
WSGI config for HtmlProfile project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HtmlProfile.settings")

application = get_wsgi_application()


#import os
#import sys
#os.environ['DJANGO_SETTING_MODULE'] = "HtmlProfile.settings"
#
#import django.core.handlers.wsgi
#
#application = django.core.handlers.wsgi.WSGIHandler()
