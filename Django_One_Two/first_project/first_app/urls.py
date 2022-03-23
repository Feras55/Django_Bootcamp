from django.conf.urls import url
from first_app import views



urlpatterns = [
    url(r'^$', views.sign_up, name='users'),
    url(r'^$', views.index, name='index'),
    url(r'^$', views.my_help, name='help'),

]