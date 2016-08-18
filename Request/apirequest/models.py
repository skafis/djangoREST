from __future__ import unicode_literals

from django.db import models

#Create your models here.
class Projects(models.Model):
	created = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100)
	description = models.TextField()

	class Meta:
		ordering = ('created',)
