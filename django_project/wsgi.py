"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
>>>>>>> d5c9750e6043eacb1599bb164f47c63b8c2c4c28
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
>>>>>>> d5c9750e6043eacb1599bb164f47c63b8c2c4c28

application = get_wsgi_application()
