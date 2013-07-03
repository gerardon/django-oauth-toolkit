# urlparse in python3 has been renamed to urllib.parse
try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from django.conf import settings
from mongoengine.base import get_document
User = get_document(settings.AUTH_USER_MODEL.split('.')[-1])
