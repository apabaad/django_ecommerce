from django.db import models

from django.conf import settings
from django.db import models
from products.models import Product

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):#defined to create new cart, and associate cart with user who is logged in but i didnt understand. 
	
	def new_or_get(self, request):
		cart_id = request.session.get('cart_id')
		qs = Cart.objects.filter(id = cart_id)
		# qs = self.get_queryset().filter(id = cart_id) Can call self also cuz it represents cart.object
		if qs.count() == 1:
			# new_obj = False
			cart_obj = qs.first()
		# if request.user.is_authenticated and cart_obj.user is None:
			if cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			# new_obj = True
			cart_obj = Cart.objects.new(request.user)
			request.session['cart_id'] = cart_obj.id
		return cart_obj

	def new(self, user):
		cart_objkt = None
		if user.is_authenticated():
			cart_objkt = user
		return self.model.objects.create(user = cart_objkt)
		

class Cart(models.Model):
	user		= models.ForeignKey(User, null = True, blank = True) #anyone can create a cart
	products 	= models.ManyToManyField(Product, blank = True)
	total		= models.DecimalField(default = 0.00, max_digits = 100, decimal_places = 2)
	updated		= models.DateTimeField(auto_now=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	
	objects 	= CartManager()
		
	def __str__(self):
		return str(self.id)