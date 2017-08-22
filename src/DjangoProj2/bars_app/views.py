# -*- coding: utf-8 -*-
# from __fsuture__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
    return HttpResponse("hello")
    #return render(request, "home.html", {})#response

def home2(request):
    html_var = 'f strings'
    html_ = """<!DOCTYPE html>
    <html lang=en>
    <head>
    </head>
    <body>
    <h1>Py Django </h1>
    <p> This is {html_var} coming through</p>
    </body>
    </html>"""
    return HttpResponse(html_)
