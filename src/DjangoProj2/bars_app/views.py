# -*- coding: utf-8 -*-
# from __fsuture__ import unicode_literals
import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
    return HttpResponse("hello")
    #return render(request, "home.html", {})#response

def home2(request):
    html_var = 'f strings'
    num = random.randint(0,1000000)
    html_ = """<!DOCTYPE html>
    <html lang=en>
    <head>
    </head>
    <body>
    <h1>Py Django </h1>
    <p> This is { html_var} coming through </p>
    </body>
    </html>"""
    return HttpResponse(html_)

def home3(request):
    num = random.randint(0,10000000)
    some_list = [num, random.randint(0,1000000), random.randint(0,1000000)]
    context = { "bool_item":True, 
    "num": num, 
    "some_list":some_list }
    return render(request, "base.html",context)
