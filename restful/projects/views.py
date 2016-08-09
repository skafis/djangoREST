from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ProjectSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Projects

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	# Api endpoint allowing users to be viewd or edited
 	queryset = User.objects.all().order_by('-date_joined')
 	serializer_class = UserSerializer

class GroupViewSets(viewsets.ModelViewSet):
	# API endpoint allowing groups to be viewd or edited
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class JSONResponse(HttpResponse):
	# an httpresponse that renders its content into Json
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] ='application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def project_list(request):
	# list all projects or create new project
	if request.method == 'GET':
		projects = Projects.objects.all()
		serializers = ProjectSerializer(projects, many=True)
		return JSONResponse(serializers.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializers = ProjectSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def project_detail(request, pk):
	# Retrive update or delete a project
	try:
		 project = Projects.objects.get(pk=pk)
	except Project.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProjectSerializer(project)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ProjectSerializer(project, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)
	elif request.method == 'DELETE':
		project.delete()
		return HttpResponse(status=204)