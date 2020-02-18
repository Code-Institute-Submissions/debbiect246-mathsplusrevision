'''
libraries added for search app.
'''
from django.conf.urls import url
from .views import do_search

'''
url pattern for search app.  This app allows a user to search
for an item in the products model.
'''
urlpatterns = [
    url(r'^$', do_search, name='search')

]
