from django.shortcuts import render,HttpResponse
from public import key
# Create your views here.
def index(req):
    return HttpResponse('这是前台界面')
