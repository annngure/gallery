from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.index,name= 'index'),
    re_path(r'^search/',views.search_results, name='search_results'),
    re_path(r'^location/<str:search_location>/',views.filter_by_location,name='location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    