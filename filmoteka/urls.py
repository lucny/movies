from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.film_list, name='film_list'),
]