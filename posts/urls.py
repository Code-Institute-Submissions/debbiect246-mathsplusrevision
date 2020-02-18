'''
libraries imported for posts app.
'''
from django.conf.urls import url, include
from django.conf.urls import url
from .views import get_posts, post_detail, posts

# urls patterns for posts app
urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^$', posts, name='posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),

]
