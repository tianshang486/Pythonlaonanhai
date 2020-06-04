"""second_pro URL Configuration

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
from app01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),

    # url(r'^books/(\d{4})/$', views.year_books),  #匹配年份的
    # # http://127.0.0.1:8000/books/2002/12/
    #
    # # url(r'^books/(\d{4})/(\d{1,2})/', views.year_month_books), #匹配年份和月份的
    # url(r'^books/(?P<year>\d{4})/(?P<month>\d{1,2})/', views.year_month_books), #匹配年份和月份的
    # {'year':'2002','month':'12'}
# http://127.0.0.1:8000/books/2001/

    url(r'^books/$', views.books),  # 匹配年份的
    # http://127.0.0.1:8000/books/2002/12/

    # url(r'^books/(\d{4})/(\d{1,2})/', views.year_month_books), #匹配年份和月份的
    url(r'^books/(?P<num>\d{4})/', views.books)
    # num:2002

]

# for url in urlpatterns:
#     ret = re.match('^books/(\d{4})/','books/2002/12/')
#     if ret:
#         break
