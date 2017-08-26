# -*- coding: utf-8 -*-
# from __fsuture__ import unicode_literals
import random
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView 

from .forms import BarsCreateForm, BarsLocationModelCreateForm
from .models import Bars_Location_Model

def bars_CreateView(request):
    #form = BarsCreateForm()
    # if request.method == 'GET':
    #     print("get data")
    # if request.method == 'POST': #PUT 
        # #print("post data")
        # #print(request.POST)
        # title    = request.POST.get("title")
        # location = request.POST.get("location")
        # cuisines = request.POST.get("cuisines")
        # obj = Bars_Location_Model.objects.create(
        #         name = title,
        #         location = location,
        #         cuisines = cuisines
        #     )



    #form = BarsCreateForm(request.POST or None)
    form = BarsLocationModelCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        #customize
        #pre save //signal
        form.save()
        #post save //signal
        # obj = Bars_Location_Model.objects.create(
        #         name     = form.cleaned_data.get('name'),
        #         location = form.cleaned_data.get('location'),
        #         cuisines = form.cleaned_data.get('cuisines')
        #     )
        return HttpResponseRedirect("/bars/")
    if form.errors:
        print(form.errors)
        errors = form.errors
        
    template_name = 'bars_app/form.html'
    context = {
        "form":form,
        "errors":errors
    }
    return render(request, template_name, context)

def bars_list_view(request):
    template_name = 'bars_app/bars_list.html'
    queryset = Bars_Location_Model.objects.all()
    context = {
        #"object_list_old": [12,14,128,256],
        "object_list": queryset
    }
    return render(request,template_name,context)

class BarsListView(ListView):
    queryset = Bars_Location_Model.objects.all()
    template_name = 'bars_app/bars_list.html'

class ItalianBarsList(ListView):
    queryset = Bars_Location_Model.objects.filter(cuisines__iexact = 'italian')
    template_name = 'bars_app/bars_list.html'

class ContinentalBarsList(ListView):
    queryset = Bars_Location_Model.objects.filter(cuisines__icontains = 'continental')
    template_name = 'bars_app/bars_list.html'

class SearchBarsList(ListView):
    template_name = 'bars_app/bars_list.html'

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Bars_Location_Model.objects.filter(
                Q(cuisines__icontains = slug) |
                Q(cuisines__iexact = slug)
                )
        else:
            queryset = Bars_Location_Model.objects.none()
        return queryset

class BarsDetailView(DetailView):
    queryset = Bars_Location_Model.objects.all()


class BarsLocationCreateView(CreateView):
    form_class = BarsLocationModelCreateForm
    template_name = 'bars_app/form.html/'
    success_url = '/bars/'
    # # def get_context_data(self,*args,**kwargs):
    # #     print(self.kwargs)
    # #     context = super(BarsDetailView,self).get_context_data(*args,**kwargs)
    # #     print(context)
    # #     return context 

    # def get_object(self,*args,**kwargs):
    #     print(self.kwargs)
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(Bars_Location_Model, id=rest_id) # pk = rest_id
    #     return obj    



# # Create your views here.
# # function based view
# def home(request):
#     return HttpResponse("hello")
#     #return render(request, "home.html", {})#response

# def home2(request):
#     html_var = 'f strings'
#     num = random.randint(0,1000000)
#     html_ = """<!DOCTYPE html>
#     <html lang=en>
#     <head>
#     </head>
#     <body>
#     <h1>Py Django </h1>
#     <p> This is { html_var} coming through </p>
#     </body>
#     </html>"""
#     return HttpResponse(html_)

# def home3(request):
#     num = None
#     some_list = [
#     random.randint(0,10000000), 
#     random.randint(0,1000000), 
#     random.randint(0,1000000)
#     ]
#     condition_bool_item = False
#     if condition_bool_item : 
#         num = random.randint(0,10000000)
#     context = { 
#     "num": num, 
#     "some_list":some_list }
#     return render(request, "home.html",context)

# def about(request):
#     context = { 
#     }
#     return render(request, "about.html",context)

# def contact(request):
#     context = { 
#     }
#     return render(request, "contact.html",context)

# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         print(kwargs)
#         context = { 
#         }
#         return render(request, "contact.html",context)

#     # def post(self, request, *args, **kwargs):
#     #     print(kwargs)
#     #     context = { 
#     #     }
#     #     return render(request, "contact.html",context)

#     # def put(self, request, *args, **kwargs):
#     #     print(kwargs)
#     #     context = { 
#     #     }
#     #     return render(request, "contact.html",context)

class HomeView(TemplateView):
    template_name = "home_old.html"

    def get_context_data(self,*args,**kwargs):
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        num = None
        some_list = [
        random.randint(0,10000000), 
        random.randint(0,1000000), 
        random.randint(0,1000000)
        ]
        condition_bool_item = False
        if condition_bool_item : 
            num = random.randint(0,10000000)
        context = { 
        "num": num, 
        "some_list":some_list }
        print(kwargs)
        return context

# class AboutView(TemplateView):
#     template_name = "about.html"

# class ContactView(TemplateView):
#     template_name = 'contact.html'


