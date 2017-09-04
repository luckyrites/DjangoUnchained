"""DjangoProj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')r
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin 
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth import views as auth_views

from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

from menu.views import HomeView 
#from bars_app.views import home,home2,home3,about,contact,ContactView,ContactViewTemplate
#from bars_app.views import HomeView, AboutView, ContactView
# from bars_app.views import (
#     HomeView,
#     #bars_list_view,
#     #BarsListView,
#     #ItalianBarsList,
#     #ContinentalBarsList,
#     #SearchBarsList,
#     #BarsDetailView,
#     #bars_CreateView,
#     #BarsLocationCreateView
#     )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('django.contrib.auth.urls')),
    url(r'^login/$',LoginView.as_view(), name='login'),
    url(r'^logout/$',LogoutView.as_view(), name='logout'),
    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    #url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'},name='login'),

    # url(r'^$',HomeView.as_view()),
    # #url(r'^home2/$',home2),
    # #url(r'^home3/$',home3,name='home3'),
    # url(r'^about/$',AboutView.as_view()), #function based view   
    # #url(r'^contact/(?P<id>\d+)/$',ContactView.as_view()),  #class based view
    # url(r'^contact/$',ContactView.as_view())
    # #url(r'^contact/$',contact),
    #url(r'^$',HomeView.as_view()),
    url(r'^$',HomeView.as_view(),name='home'),
    # url(r'^home/$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^bars/',include('bars_app.urls',namespace='bars_app')),
    url(r'^items/',include('menu.urls',namespace='menu')),
    url(r'^profile-follow/$',ProfileFollowToggle.as_view(),name='follow'),
    url(r'^u/',include('profiles.urls',namespace='profiles')),
    # #url(r'^bars/$',bars_list_view),
    # url(r'^bars/$',BarsListView.as_view(), name ='bars'),
    # url(r'^bars/italian/$',ItalianBarsList.as_view()),
    # url(r'^bars/continental/$',ContinentalBarsList.as_view()),
    # url(r'^bars/SearchCuisine/(?P<slug>\w+)/$',SearchBarsList.as_view()),
    # #url(r'^bars/(?P<pk>\d+)/$',BarsDetailView.as_view()),
    # # url(r'^bars/(?P<rest_id>\w+)/$',BarsDetailView.as_view()),
    
    # #url(r'^bars/create/$',bars_CreateView),
    # url(r'^bars/create/$',BarsLocationCreateView.as_view(), name ='create'),
    
    # url(r'^bars/(?P<slug>[\w-]+)/$',BarsDetailView.as_view(), name ='bars-detail'),



    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'), name ='contact'),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'), name='about'),
]
 