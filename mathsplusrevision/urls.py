"""mathsplusrevision URL Configuration

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
# imported libraries for project
# url needed to handle urls
from django.conf.urls import url, include
# redirectview needed for redirecting users to another page when necessary
from django.views.generic import RedirectView
# serve needed to serve static files
from django.views.static import serve
# admin needed for the django dashboard
from django.contrib import admin
# path needed to direct data along correct path
from django.urls import path
# accounts needed to import account urls
from accounts import urls as urls_accounts
# urls for products imported
from products import urls as urls_products
# urls for posts imported
from posts import urls as urls_posts
# urls for cart imported
from cart import urls as urls_cart
# urls from search app imported
from search import urls as urls_search
# urls from checkout app imported
from checkout import urls as urls_checkout
# urls from product app imported
from products.views import all_products
# urls from all views to host static files imported
from django.views import static
# media root needed to handle all media files
from .settings import MEDIA_ROOT

# url patterns for all pages on website

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', all_products, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    #url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include(urls_posts)),


    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
