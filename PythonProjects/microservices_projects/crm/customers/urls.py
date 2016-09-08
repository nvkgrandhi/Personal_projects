from django.conf.urls import url, include, patterns
from customers import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/', views.register_customers, name='register_customers'),
    url(r'^customers/', views.list_all_customers, name='list_all_customers'),
]