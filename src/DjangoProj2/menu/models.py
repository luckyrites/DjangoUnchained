# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.core.urlresolvers import reverse

from django.db import models

from bars_app.models import Bars_Location_Model
from django.contrib.auth.models import User

from django.db.models.signals import pre_save, post_save
# Create your models here.
class Item(models.Model):
	# associations
	#user = models.ForeignKey(settings.AUTH_USER_MODEL)
	user = models.ForeignKey(User,related_name='Items')
	bars = models.ForeignKey(Bars_Location_Model, related_name='Items')
	# item stuff
	name      = models.CharField(max_length=120)
	contents  = models.TextField(help_text='Separate each item by comma')
	excludes  = models.TextField(blank = True, null = True, help_text='Separate each item by comma')
	public 	  = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated   = models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ['-updated','-timestamp'] # Item.objects.all()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return f"/bars/{self.slug}"
		return reverse('menu:detail', kwargs={'pk': self.pk })

	def get_contents(self):
		return self.contents.split(',')

	def get_excludes(self):
		return self.excludes.split(',')	
