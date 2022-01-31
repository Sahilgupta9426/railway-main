from django.urls import path,include,re_path
from . import views

urlpatterns = [
    
    re_path(r'^home/$', views.home,name="home"),
    
    re_path(r'^home/searchform/$', views.searchform,name="searchform"),
    re_path(r'^home/(?P<pk>\d+)/customer/$', views.customer,name="customer"),
    # re_path(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    
]