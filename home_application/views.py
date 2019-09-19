# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
# 装饰器引入 from blueapps.account.decorators import login_exempt
from blueapps.account.decorators import login_exempt
from django.forms import forms


#################
import  pandas as pd
from home_application.pre_check import *
 
    
def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')


def contact(request):
    """
    联系我们
    """
    return render(request, 'home_application/contact.html')
    
def blueking(request):
    return render(request, 'home_application/blueking.html')

def test1(request):
    return render(request,'home_application/1.html')
    
@login_exempt
def test2(request):
    if request.method == 'POST':
        a =  request.FILES.get('upload_csv')
        #这玩意是个class
        try:
            df = pd.read_csv(a,encoding='gbk')
            inner_ip_list = df['内网IP'].values
            a = Sync(inner_ip_list)
            a.test()
        except ValueError:
            print('csv文件没上传')
        try:
            passwd = request.POST.get('passwd')
            domain = request.POST.get('domain')
            
            print(passwd)
        except ValueError:
            print('密码没填')
        inner_ip_list = df['内网IP'].values
        a.check_contrl_ip(inner_ip_list,request.POST.get('inner_ctrl_ip'))
        return render(request,'home_application/blueking.html')
    else:
        return render(request,'home_application/home.html')
