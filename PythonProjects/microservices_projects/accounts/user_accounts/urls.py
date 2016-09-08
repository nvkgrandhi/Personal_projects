from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^$/', views.home, name='home'),
    url(r'^register/', views.create_user, name='create_user'),
    url(r'^users/', views.list_users, name='list_users'),
]