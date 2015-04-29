from django.conf.urls import patterns, url

from noticeboard import views

urlpatterns = patterns('',
	
	url(r'^$', views.events, name = "events"),
	url(r'^(?P<event_id>\d+)/$', views.event_detail, name = "event_detail")
	)