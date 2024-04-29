from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('<h1>Hello world!</h1>')

def test(request):
    return HttpResponse('<h3>Test page</h3>')