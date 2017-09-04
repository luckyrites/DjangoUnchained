# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db.models import Q
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_cuisines
from django.core.urlresolvers import reverse


User = settings.AUTH_USER_MODEL
# Create your models here.

class Bars_Location_ModelQuerySet(models.query.QuerySet):
	def search(self,query): #Bars_Location_Model.objects.all().search(query) #Bars_Location_Model.objects.filter(something).search(query)
		if query:
			query = query.strip()
			return self.filter(
				Q(name__icontains=query)|
				Q(location__icontains=query)|
				Q(cuisines__icontains=query)|
				Q(Items__name__icontains=query)|
				Q(Items__contents__icontains=query)
			 	).distinct()
		return self

class BarsLocationModelManager(models.Manager):
	def get_queryset(self):
		return Bars_Location_ModelQuerySet(self.model, using=self._db)
	def search(self,query): # Branch_Location_Model.objects.search()
		return self.get_queryset().filter(name__icontains=query) 

class Bars_Location_Model(models.Model):
	owner     = models.ForeignKey(User,related_name='Bars') #Django Models Unleashed JOINCFE.com
	name 	  = models.CharField(max_length=120)
	location  = models.CharField(max_length=120,null = True, blank = True)
	cuisines  = models.CharField(max_length=450,null = True, blank = True, validators=[validate_cuisines])
	#my_date_field = models.DateTimeField(auto_now=False,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated   = models.DateTimeField(auto_now = True)
	slug 	  = models.SlugField(null=True, blank=True)

	objects = BarsLocationModelManager()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return f"/bars/{self.slug}"
		return reverse('bars_app:detail', kwargs={'slug': self.slug })

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