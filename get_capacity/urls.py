# _*_ coding: utf-8 _*_
from django.conf.urls import url

from get_capacity import views

urlpatterns = (
    url(r'^$', views.test),
    url(r'^get_ip_by_appid/$', 'get_ip_by_appid'),
    url(r'^get_task_list/$', 'get_task_id_appid'),
    
    url(r'^execute_task/$', 'execute_task'),
    url(r'^get_capacity/$', 'get_capacity'),
    
    url(r'^chartdata/$', 'get_capacity_chartdata'),
)