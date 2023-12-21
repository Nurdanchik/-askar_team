"""
WSGI config for puddle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puddle.settings')

application = get_wsgi_application()

# app = application
# {
#     "builds": [{
#         "src": "puddle/wsgi.py",
#         "use": "@vercel/python",
#         "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
#     }],
#     "routes": [
#         {
#             "src": "/(.*)",
#             "dest": "puddle/wsgi.py"
#         }
#     ]
# }