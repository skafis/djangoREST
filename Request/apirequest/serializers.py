from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.forms import widgets
from .models import Projects


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url','name')


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Projects
		fields = ('id','title','description')