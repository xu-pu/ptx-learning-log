from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render_to_response

def hello_world(request):
    return HttpResponse("Hello, World")

def html_hello_world(request):
    return HttpResponse()

def template_hello_world(request):
    return HttpResponse()

def template_shortcut(request):
    return render_to_response()
