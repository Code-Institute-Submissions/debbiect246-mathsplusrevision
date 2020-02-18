'''
urls added for cart app for adding items to cart and 
then changing items on cart if user wants to do this 
before checkout.
'''
from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
]
