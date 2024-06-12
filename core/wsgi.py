import os
from django.core.wsgi import get_wsgi_application

# Check for the environment variable to decide which settings to use
if os.getenv('DJANGO_ENV') == 'AZURE':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings_local')

application = get_wsgi_application()
