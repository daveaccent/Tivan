from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name="detail"),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.edit, name='edit'),
]