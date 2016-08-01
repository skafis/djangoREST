from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializers):
	class Meta:
		model = Group
		fields = ('url','username', 'email','groups')

class GroupSerializer( serializers.HyperlinkedModelSerializers):
	class Meta:
		model = Group
		fields = ('url','name')