from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
	url(r'^projects/$', views.project_list),
	url(r'^projects/(?P<pk>[0-9]+)$', views.project_detail),
]

urlpatterns=format_suffix_patterns(urlpatterns)