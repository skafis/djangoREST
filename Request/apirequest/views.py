from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectSerializer

# Create your views here.
@api_view (['GET', 'POST'])
def project_list(request):
	# listing all snippets or creating new
	if request.method == 'GET':
		project = Projects.objects.all()
		serializer = ProjectSerializer(project, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_	BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def project_detail(request, pk):
	# retreive update or delete project instance
	try:
		project =Projects.objects.get(pk=pk)
	except Projects.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ProjectSerializer(project)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ProjectSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


