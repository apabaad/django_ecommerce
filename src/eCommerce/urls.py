"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin


#commented because we have created a decicated urls for the product app
# from products.views import (ProductListView, 
#     product_list_view, 
#     ProductDetailView, 
#     product_detail_view,
#     ProductFeaturedListView)

from .views import HomePage, AboutPage, ContactPage, LoginPage, RegisterPage

urlpatterns = [
	url(r'^$', HomePage),
	url(r'^homepage/$', HomePage),
	url(r'^about/$', HomePage),
	url(r'^contact/$', ContactPage),
    url(r'^login/$', LoginPage),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', RegisterPage),
    # url(r'^products-fbv/$', product_list_view),
    # url(r'^products/$', ProductListView.as_view()), #making the ClassBasedView a callable item with as_view()
    # url(r'^detail-fbv/(?P<id>\d+)$', product_detail_view),
    # url(r'^products/detail/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
   
    url(r'^products/', include("products.urls")),
    url(r'^search/', include("search.urls", namespace='search')),
    url(r'^cart/', include("carts.urls", namespace='cart'))

    
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)