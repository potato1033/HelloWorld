from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
'''
def hello(request):
    return HttpResponse("Hello world ! ")
'''

def index(request):
    return HttpResponse("123456789 ! ")

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def base(request):
    context          = {}
    context['base'] = 'Hello Base!'
    return render(request, 'base.html', context)