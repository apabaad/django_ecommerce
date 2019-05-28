from django.conf.urls import url

from .views import (
    ProductListView, 
   # product_list_view, 
    ProductDetailView, 
    # product_detail_view,
    ProductFeaturedListView)


urlpatterns = [
    url(r'^products-fbv/$', ProductListView),
    
    # for list
    url(r'^$', ProductListView.as_view()), #making the ClassBasedView a callable item with as_view()
    
    # url(r'^detail-fbv/(?P<id>\d+)$', product_detail_view),
    url(r'^detail/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedListView.as_view()),

]


