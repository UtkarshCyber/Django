"""
ASGI config for django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> d5c9750e6043eacb1599bb164f47c63b8c2c4c28
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
>>>>>>> d5c9750e6043eacb1599bb164f47c63b8c2c4c28

application = get_asgi_application()
