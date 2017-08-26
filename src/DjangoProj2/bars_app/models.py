# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_cuisines

# Create your models here.
class Bars_Location_Model(models.Model):
	name 	  = models.CharField(max_length=120)
	location  = models.CharField(max_length=120,null = True, blank = True)
	cuisines  = models.CharField(max_length=450,null = True, blank = True, validators=[validate_cuisines])
	#my_date_field = models.DateTimeField(auto_now=False,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated   = models.DateTimeField(auto_now = True)
	slug 	  = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name # obj.title 

def bars_pre_save_receiver(sender, instance, *args, **kwargs):
	# print('saving..')
	# print(instance.timestamp)
	instance.cuisines.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance) 

# def bars_post_save_receiver(sender, instance, created, *args, **kwargs):
# 	print('Saved')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()

pre_save.connect(bars_pre_save_receiver, sender=Bars_Location_Model)

# post_save.connect(bars_post_save_receiver, sender=Bars_Location_Model)