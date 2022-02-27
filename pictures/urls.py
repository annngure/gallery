from django.urls import path,re_path
from . import views

urlpatterns=[
    re_path('^$',views.index,name= 'index'),
    re_path(r'^search/',views.search_results, name='search_results')
]