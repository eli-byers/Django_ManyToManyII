from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newUser$', views.newUser),
    url(r'^user/(?P<id>[0-9]+)$', views.viewUser),
]
