from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Photographer, Location, Category,Image
# Create your views here.

def index(request):
    category=Category.objects.all()
    # photographer=Photographer.object.all()
    image=Image.objects.all()
    location = Location.all_locations()
    title = 'Ultimate'
    return render(request,'index.html',{"title":title , "location":location,"image":image,"category":category})

def search_results(request):
    location = Location.objects.all()
    if 'category'in request.GET and request.GET['category']:
        search_category=request.GET.get("category")
        searched_category = Image.search_image(search_category)
        message=f"{search_category}"
        
        return render(request, 'search.html',{"message":message,"image":searched_category,"location":location})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def filter_by_location (request,location_id):
    title='Location'
    location =Location.object.all()
    image= Image.filter_by_location(id=location_id)

    return render(request, 'location.html',{"image":image,"location":location_id})
