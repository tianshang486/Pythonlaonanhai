from django.urls import reverse
from django.shortcuts import (
    redirect,HttpResponse,render
)
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):
    settings.WHITE_LIST
    def process_request(self,request):
        print('MD1 process_request')
        print(request.META.get('REMOTE_ADDR')) #127.0.0.1 客户端ip地址


    def process_view(self, request, view_func, view_args, view_kwargs):

        print('MD1 process_view',view_func)

    def process_response(self, request,response):
        print('MD1 process_response', response)
        return response
    def process_exception(self, request, exception):
        print('md1 错误')

    def process_template_response(self, request, response):
        print('md1 process_template_response')
        return response
class MD2(MiddlewareMixin):

    def process_request(self, request):
        print('md2 process_request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('md2 process_view', view_func.__name__)
        # return HttpResponse('ooo')

    def process_response(self, request, response):
        print('md2 process_response', response)
        return response

    def process_exception(self, request, exception):
        print('md2 错误')

    def process_template_response(self, request, response):
        print('md2 process_template_response')

        return response

