from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

def get_content(request, title):
    items = ['This is item %d' % num for num in range(0,8)]
    return render_to_response('for-loop.html', {'title':title, 'string_list':items})

