from django.conf.urls import url
from blog.views import post_list 
from blog.views import post_detail

from django.contrib import admin

 

urlpatterns = [
        url(r'^$',post_list),
        url(r'^(?P<id>\d+)/$', post_detail),
        
]
