# urls for checkout app recorded here.-->
from django.conf.urls import url
from .views import checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]
