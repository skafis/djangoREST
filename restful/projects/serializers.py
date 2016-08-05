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


class projectSerializer(serializers.Serializer):
	primary_key = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
	description = serializers.CharField()

	def create(self, validated_data):
		""" create and return project instance given validated date"""
		return project.objects.create(**validated_data)

	def update(self, instance, validated_data):
		# update and return existing project instance given validated data
		instance.title = validated_data.get('title', instance.title)
		instance.description = validated_data.get('description',instance.description)
		instance.save()
		return instance