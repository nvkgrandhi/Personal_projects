from django.conf.urls import url, patterns, include
from products import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_product/', views.add_product, name='add_product'),
    url(r'^list_all_products/', views.list_all_products, name='list_all_products'),
]
