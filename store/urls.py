from django.conf.urls import url
from . import views

from django.views.static import serve

urlpatterns = [
    url(r'^$',views.store,name='store'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^checkout/$',views.checkout,name='checkout'),
    url(r'^update_item/$',views.updateItem,name="update_item"),
    url(r'^process_order/$',views.processOrder,name="process_order"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]