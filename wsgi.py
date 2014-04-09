from __future__ import unicode_literals

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
