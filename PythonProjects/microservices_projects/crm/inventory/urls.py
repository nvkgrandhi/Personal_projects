from django.conf.urls import url, patterns, include
from inventory import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
]