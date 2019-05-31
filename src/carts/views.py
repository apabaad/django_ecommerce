from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product

#commented this function and made model manager to create cart object
# def cart_create():
# 	cart_obj = Cart.objects.create()
# 	return cart_obj

def cart_home(request):
	cart_item = Cart.objects.new_or_get(request)

	'''commented this because we created model manager to handle this. since this is not the
	only place we need cart create or get get session in the future. From model manager, 
	we can use new_or_get in any view.'''

	# cart_id = request.session.get('cart_id')
	# qs = Cart.objects.filter(id = cart_id)
	# if qs.count() == 1:
	# 	cart_obj = qs.first()
	# 	# if request.user.is_authenticated and cart_obj.user is None:
	# 	if cart_obj.user is None:
	# 		cart_obj.user = request.user
	# 		cart_obj.save()
	# else:
	# 	cart_obj = Cart.objects.new(request.user)
	# 	request.session['cart_id'] = cart_obj.id

	products 	= cart_item.products.all()
	cart_total 		= 0
	for x in products:
		cart_total+= x.price
	cart_item.total 		= cart_total
	cart_item.save()

	return render(request, 'carts/home.html', {"cart" : cart_item})

def cart_update(request):
	product_id 	= request.POST.get('product_id')
	product_obj = Product.objects.get(id = product_id)
	
	cart_obj	= Cart.objects.new_or_get(request)
	if product_obj in cart_obj.products.all():
		cart_obj.products.remove(product_obj)
		a = cart_obj.products.count()
		request.session['total_cart_items'] = a
	else:
		cart_obj.products.add(product_obj)
		a = cart_obj.products.count()
		request.session['total_cart_items'] = a


	return redirect("cart:home")


