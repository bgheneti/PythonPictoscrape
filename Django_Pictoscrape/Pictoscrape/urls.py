#PictoScrape/urls.py

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^fanfics/', include('fanfics.urls', namespace="fanfics")),
    url(r'^admin/', include(admin.site.urls)),
)