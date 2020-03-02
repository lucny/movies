from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.film_list, name='film_list'),
     url(r'^film/(?P<pk>[0-9]+)/$', views.film_detail, name='film_detail'),
]