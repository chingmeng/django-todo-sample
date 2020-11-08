from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from rest_framework.routers import *
from rest_framework.schemas import get_schema_view

from .views import *

schema_view = get_schema_view(title='Todo API')

router = routers.DefaultRouter()
urlpatterns = [
    url(r'^', include(router.urls)),
    path('api/', TodoAPI.as_view())
]

# The API URLs are now determined automatically by the router.
if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
