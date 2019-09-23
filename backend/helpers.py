"""Contains helper functions being used in several places"""

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

def get_image_url(imgPath, request):
    return "".join([get_current_site(request).domain, settings.MEDIA_URL,str(imgPath)])
