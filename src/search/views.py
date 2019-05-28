from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product


class SearchProductView(ListView):

	template_name = 'search/view.html'

	def get_queryset(self):
		request = self.request
		query = request.GET.get('search_query', None)
		
		if query is not None:
			return Product.objects.search(query)
		return Product.objects.featured()

		'''
		__icontains = fields that contains this
		__iexact = fields that is exactly this
		'''