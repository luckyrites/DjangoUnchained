from django.conf.urls import url

from .views import (
    BarsLocationCreateView,
    BarsDetailView,
    BarsListView,
    BarsLocationUpdateView,
    json_index,
    validate_name,
    #bars_list_view,
    #ItalianBarsList,
    #ContinentalBarsList,
    #SearchBarsList,
    #bars_CreateView,
    )

urlpatterns = [
    #url(r'^italian/$',ItalianBarsList.as_view(), name='list-italian'),
    #url(r'^continental/$',ContinentalBarsList.as_view(), name='list-continental'),
    #url(r'^SearchCuisine/(?P<slug>\w+)/$',SearchBarsList.as_view(), name='search'),
    ##url(r'^bars/create/$',bars_CreateView),


    url(r'^create/$',BarsLocationCreateView.as_view(), name ='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$',BarsLocationUpdateView.as_view(), name ='edit'),
    url(r'^(?P<slug>[\w-]+)/$',BarsLocationUpdateView.as_view(), name ='detail'),
    url(r'^$',BarsListView.as_view(), name ='list'),
    
    #for ajax calls
    url(r'^validate_name$',validate_name, name='validate_name'),
    url(r'^data$',json_index,name='json'),
]
 