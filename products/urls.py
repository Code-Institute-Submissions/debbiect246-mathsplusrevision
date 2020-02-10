from django.conf.urls import url, include
from .views import all_products

# url pattern for products page

urlpatterns = [

    url(r'^products', all_products, name='products'),


]
