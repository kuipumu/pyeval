"""
Project URLS
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""

from django.urls import include, path
from rest_framework import routers

from base.views import LogViewSet, RoleViewSet, UserViewSet, login_view

# Add Django REST framework default router.
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = routers.DefaultRouter()
# Add user viewset.
router.register(r'users', UserViewSet)
# Add role viewset.
router.register(r'roles', RoleViewSet)
# Add log viewset.
router.register(r'logs', LogViewSet)

# Add project URL patterns.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', login_view)
]
