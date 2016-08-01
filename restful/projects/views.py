from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
# Create your views here.

class UserViewSets (viewsets.ModelViewSet):
	# Api endpoint allowing users to be viewd or edited
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSets(viewsets.ModelViewSet):
	# API endpoint allowing groups to be viewd or edited
	queryset = Group.objects.all()
	serializer_class = GroupSerializer