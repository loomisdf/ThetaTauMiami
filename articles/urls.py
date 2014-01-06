'''
Created on Jan 6, 2014

@author: kyle
'''
from django.conf.urls import patterns, url

from articles import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^service/$', views.service, name='service'),
    url(r'^pd/$', views.professional_development, name='professional_development'),
    url(r'^social/$', views.social, name='social'),
)