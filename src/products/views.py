from django.shortcuts import render
from django.http import Http404
from .models import Product
from django.views.generic import ListView, DetailView
from carts.models import Cart



# views can be of two types: class based and function based. in this page, we have both.

#class based view

class ProductListView(ListView):  				#this class based view inherits ListView we imported.
	queryset = Product.objects.all() 			#This is how we make queryset.

	# template_name= 'products/list.html'

'''every class based view has this method given below to pass the context to the template. 
	Not sure: In default, it looks for query_list in template. eg: for qs in query_list
	we can get rid of the method below if we use query_list in the template'''

	#to pass context to the template
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	return context
	# 	print ("context")
	


#function based view

# def product_list_view(request):
# 	queryset = Product.objects.all()
# 	context = {
# 	'object_list' : queryset
# 	}
# 	return render(request, "products/product_list.html", context)
		

class ProductDetailView(DetailView):  				
	queryset 	= Product.objects.all()
	# template_name = "products/product_detail.html"

	'''# to send context from cart.models. aafno model(products.model) ko context classbased 
	# view le aafai pathauchha.'''
	def get_context_data(self, *args, **kwargs):
		context 	= super(ProductDetailView, self).get_context_data(*args, **kwargs)
		request		= self.request
		cart_obj	= Cart.objects.new_or_get(request)
		context['cart'] = cart_obj
		return context

# def product_detail_view(request, id):
# 	queryset = Product.objects.get(id = id)
# 	context = {
# 	'object' : queryset
# 	}
# 	return render(request, "products/product_detail.html", context)
	


class ProductFeaturedListView(ListView):
	# template_name = "products/list.html"   Automatically looks for product_list if not overriden.

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()

# class ProductFeaturedDetailView(DetailView):
# 	template_name = "products/featured-detail.html"

# 	def get_queryset(self, *args, **kwargs):
# 		request = self.request
# 		return Product.objects.featured()

# def ProductList(request):
# 	queryset = Product.objects.all()
# 	context = {
# 	'ObjectList' : queryset
# 	}
# 	return render(request,"products/list.html", context)

# def ProductDetail(request, id):
	
# 	# instance = Product.objects.get(id=id)

# 	instance = Product.objects.get_by_id(id)
# 	if instance is None:
# 		raise Http404("Product not found")
	
	
# 	# qs = Product.objects.filter(id=id)
# 	# if qs.exists() and qs.count() == 1:
# 	# 	instance = qs.first()
# 	# else:
# 	# 	raise Http404("Product not found")

# 	context = {
# 		'object' : instance
# 	}

# 	return render(request,"products/detail.html", context)