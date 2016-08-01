from __future__ import unicode_literals

from django.db import models

# Create your models here.
class projects(models.Model):
	created = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100)
	code = models.TextField()

	class meta:
		ordering = ('created')
