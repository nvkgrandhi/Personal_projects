from django.conf.urls import url, include, patterns
from employee import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_employee/', views.add_employee, name='add_employee'),
]