from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^projects/$', views.project_list),
	url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
]