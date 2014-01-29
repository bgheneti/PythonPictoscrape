from django.conf.urls import patterns, url

from fanfics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), 
    url(r'^(?P<fanfic_id>\d+)/$', views.detail, name='detail'),
    url(r'^createNew$', views.createNew, name='createNew'),
    url(r'^createURL$', views.createURL, name='createURL'),
)