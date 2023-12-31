import os

from django.core.wsgi import get_wsgi_application

if os.path.isfile('env.py'):
    import env

development = os.environ.get("DEVELOPMENT", False)

if development == 'True':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod_settings')

application = get_wsgi_application()
