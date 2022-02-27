from django.shortcuts import render
from django.http import HttpResponse
from .models import Photographer, Location, Category
# Create your views here.

def index(request):
    locations = Location.objects.all()
    title = 'Ultimate'
    return render(request,'index.html',{"title":title , "locations":locations})

def search_results(request):
    if 'category'in request.GET and request.GET['category']:
        search_term=request.GET.get("category")
        saerched_category = Category.search_by_title(search_term)
        message=f"{search_term}"

        return render(request, 'search.html',{"message":message,"category":searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html'{"message":message})