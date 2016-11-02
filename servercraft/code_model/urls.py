URLS=r'''
from django.conf.urls import patterns, include, url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^handler/start/$', views.handler_start),
    url('^handler/(\d+)/$', views.handler_detail),
    url('^handler/download/(\d+)/$', views.handler_download),

	]
'''