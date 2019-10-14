from django.conf.urls import url, include
from . import urls_reset
from .views import blog


urlpatterns = [
    url(r'^blog/$', blog, name='blog'),
]
