"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views as rest_framework_views
from rest_framework_swagger.views import get_swagger_view

from toys.views import ToyViewSet, BrandViewSet, CategoryViewSet
from customers.views import CustomerViewSet, CustomAuthToken, HoppListViewSet, SubscriptionViewSet

# Set up user
User = get_user_model()

# Set up drf routing
router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'toys', ToyViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'hopplist', HoppListViewSet)
router.register(r'subscription', SubscriptionViewSet)

schema_view = get_swagger_view(title='Playhopp API')


urlpatterns = [
    # To prefix for nginx
    url(r'^api/', include([
            url(r'^token_login/$', CustomAuthToken.as_view(), name='token_login'),
            url('admin/', admin.site.urls),
            url(r'api-auth/', include('rest_framework.urls')),
            url(r'^', include(router.urls)),
            url(r'^swagger', schema_view),
    ]))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
