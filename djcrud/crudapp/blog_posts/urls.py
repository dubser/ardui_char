"""blog_posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
app_name = 'blog_posts'

from django.conf.urls import url
from blog_posts import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^edit/(?P<pk>\d+)$', views.post_update, name='post_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
]