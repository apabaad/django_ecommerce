import os
# from django.utils.text import slugify
from django.db import models
import random
from django.db.models import Q # for the '?q=' that we see in the get URL


# function to extract name and extension

def get_filename_and_ext(filepath):
	base_name	= os.path.basename(filepath)
	name, ext 	= os.path.splitext(base_name)
	return name, ext

#function to change name of the file and generate path to save

def upload_img_path(instance, filename):
	new_filename	= random.randint(1, 99999999)
	name, ext 		= get_filename_and_ext(filename)
	final_filename	= "{new_filename}{ext}".format(new_filename = new_filename, ext = ext)
	return "products/{}".format(final_filename)

#creating model manager
class ProductManager(models.Manager):
	
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None 

	def featured(self):
		return self.get_queryset().filter(featured=True) #Product.objects of queryset == self.get_queryset() of this
		

	def search(self, query):
		lookups = Q(title__icontains = query) | Q(description__icontains = query)
		return self.get_queryset().filter(lookups).distinct()

class Product(models.Model):
	title 			= models.CharField(max_length = 20)
	# slug			= models.SlugField(unique = True, default = "ram")
	description 	= models.TextField()
	price 			= models.DecimalField(decimal_places=2, max_digits=20)
	image 			= models.ImageField(upload_to = upload_img_path, null = True, blank = True)
	featured		= models.BooleanField(default = False)

	objects 		= ProductManager()

	
	# for slug
	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.title)
	# 	super(Article, self).save(*args, **kwargs)

	
	
	# show item by 'title' in the django administration datatabase
	def __str__(self):
		return self.title
	