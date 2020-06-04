"""supercrm URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from sales import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 登录
    url(r'^login/', views.login,name='login'),
    # 注册
    url(r'^register/', views.register,name='register'),
    # 首页
    url(r'^home/', views.home,name='home'),

    #所有客户信息展示  #http://127.0.0.1:8000/customers/4/?page=3
    # url(r'^customers/(\d+)/', views.customers,name='customers'),
    url(r'^customers/', views.customers,name='customers'),
    # 我的客户
    url(r'^mycustomers/', views.customers,name='mycustomers'),

    # 添加客户
    # url(r'^add_customer/', views.add_customer,name='add_customer'),
    url(r'^add_customer/', views.add_edit_customer,name='add_customer'),
    # 编辑客户
    # url(r'^edit_customer/(\d+)/', views.edit_customer,name='edit_customer'),
    url(r'^edit_customer/(\d+)/', views.add_edit_customer,name='edit_customer'),


]
