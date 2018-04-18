from django.views.generic import View
from django.shortcuts import render

# Create your views here.


class Common(View):

    http_method_names = ['get', 'post']




class Api(Common):
    http_method_names = ['get', 'post', 'put', 'delete']
