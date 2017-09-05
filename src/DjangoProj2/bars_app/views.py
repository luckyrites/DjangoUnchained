# -*- coding: utf-8 -*-
# from __fsuture__ import unicode_literals
import random
from django.contrib.auth.decorators import login_required #for function based view
from django.contrib.auth.mixins import LoginRequiredMixin #for class based view
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView 

from .forms import BarsCreateForm, BarsLocationModelCreateForm
from .models import Bars_Location_Model
from django.http import JsonResponse
from django.core import serializers

# @login_required() #(login_url='/login/') #already set in base.py
# def bars_CreateView(request):
#     #form = BarsCreateForm()
#     # if request.method == 'GET':
#     #     print("get data")
#     # if request.method == 'POST': #PUT 
#         # #print("post data")
#         # #print(request.POST)
#         # title    = request.POST.get("title")
#         # location = request.POST.get("location")
#         # cuisines = request.POST.get("cuisines")
#         # obj = Bars_Location_Model.objects.create(
#         #         name = title,
#         #         location = location,
#         #         cuisines = cuisines
#         #     )



#     #form = BarsCreateForm(request.POST or None)
#     form = BarsLocationModelCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         if request.user.is_authenticated():
#             user = request.user
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#             #customize
#             #pre save //signal
#             #form.save()
#             #post save //signal
#             # obj = Bars_Location_Model.objects.create(
#             #         name     = form.cleaned_data.get('name'),
#             #         location = form.cleaned_data.get('location'),
#             #         cuisines = form.cleaned_data.get('cuisines')
#             #     )
#             return HttpResponseRedirect("/bars/")
#         else:
#             return HttpResponseRedirect("/login/")
#     if form.errors:
#         # if request.user.is_authenticated():

#         print(form.errors)
#         errors = form.errors
        
#     template_name = 'bars_app/form.html'
#     context = {
#         "form":form,
#         "errors":errors
#     }
#     return render(request, template_name, context)

# def bars_list_view(request):
#     template_name = 'bars_app/bars_list.html'
#     queryset = Bars_Location_Model.objects.all()
#     context = {
#         #"object_list_old": [12,14,128,256],
#         "object_list": queryset
#     }
#     return render(request,template_name,context)

def json_index(request):
    bars_as_json = serializers.serialize('json',Bars_Location_Model.objects.all())#filter(name__iexact=name))
    context = bars_as_json
    return HttpResponse(context,content_type = 'json')

def validate_name(request):
    name = request.GET.get('name',None)
    print(name)
    data = {
        'is_taken': Bars_Location_Model.objects.filter(name__iexact=name).exists()
    }
    if data['is_taken']:
        data['error_msg'] = "The Bar named : " + name + " alredy exists !!"
    return JsonResponse(data)

class BarsListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        #print(self.request.user) 
        queryset = Bars_Location_Model.objects.filter(owner=self.request.user)
        return queryset
    template_name = 'bars_app/bars_list.html'

# class ItalianBarsList(ListView):
#     queryset = Bars_Location_Model.objects.filter(cuisines__iexact = 'italian')
#     template_name = 'bars_app/bars_list.html'

# class ContinentalBarsList(ListView):
#     queryset = Bars_Location_Model.objects.filter(cuisines__icontains = 'continental')
#     template_name = 'bars_app/bars_list.html'

# class SearchBarsList(ListView):
#     template_name = 'bars_app/bars_list.html'

#     def get_queryset(self):
#         print(self.kwargs)
#         slug = self.kwargs.get('slug')
#         if slug:
#             queryset = Bars_Location_Model.objects.filter(
#                 Q(cuisines__icontains = slug) |
#                 Q(cuisines__iexact = slug)
#                 )
#         else:
#             queryset = Bars_Location_Model.objects.none()
#         return queryset

class BarsDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        queryset = Bars_Location_Model.objects.filter(owner=self.request.user)
        return queryset

class BarsLocationCreateView(LoginRequiredMixin, CreateView):
    form_class = BarsLocationModelCreateForm
    #login_url = '/login_fromClassView/' #already set in base.py
    login_url = '/login/'
    template_name = 'bars_app/form.html/'
    #success_url = '/bars/'  #instead we'll define get_absolute_url in model

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        #instance.save()
        return super(BarsLocationCreateView,self).form_valid(form)  

    def get_context_data(self, *args, **kwargs):
        context = super(BarsLocationCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Bar'
        return context

    def get_form_kwargs(self):
        kwargs = super(BarsLocationCreateView, self).get_form_kwargs()
        kwargs.update({'owner': self.request.user })
        #kwargs['user'] = self.request.user
        ##kwargs['instance'] = Item.objects.filter(user = self.request.user).first()
        return kwargs

# class BarsLocationUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'bars_app/detail-update.html'
#     form_class = BarsLocationModelCreateForm

#     def get_queryset(self):
#         return Bars_Location_Model.objects.all() #.filter(owner = self.request.user)


class BarsLocationUpdateView(LoginRequiredMixin, UpdateView):
    #template_name = 'bars_app/form.html'
    template_name = 'bars_app/detail-form.html'
    form_class = BarsLocationModelCreateForm
    #login_url = '/login/'

    def get_queryset(self):
        return Bars_Location_Model.objects.filter(owner = self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(BarsLocationUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Bar'
        return context

    def get_form_kwargs(self):
        kwargs = super(BarsLocationUpdateView, self).get_form_kwargs()
        kwargs['owner'] = self.request.user
        #kwargs['instance'] = Item.objects.filter(user = self.request.user).first()
        return kwargs

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

# class HomeView(TemplateView):
#     template_name = "home_old.html"

#     def get_context_data(self,*args,**kwargs):
#         context = super(HomeView,self).get_context_data(*args,**kwargs)
#         num = None
#         some_list = [
#         random.randint(0,10000000), 
#         random.randint(0,1000000), 
#         random.randint(0,1000000)
#         ]
#         condition_bool_item = False
#         if condition_bool_item : 
#             num = random.randint(0,10000000)
#         context = { 
#         "num": num, 
#         "some_list":some_list }
#         print(kwargs)
#         return context

# class AboutView(TemplateView):
#     template_name = "about.html"

# class ContactView(TemplateView):
#     template_name = 'contact.html'


