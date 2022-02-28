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
    image=Image.objects.all()
    location = Location.all_locations()
    if 'category'in request.GET and request.GET['category']:
        search_term=request.GET.get("category")
        # searched_category = Category.objects.filter(name__name__icontains = search_term)
        searched_category = Category.search_by_title(search_term)
        message=f"{search_term}"

        return render(request, 'search.html',{"message":message,"category":searched_category,"location":location,"image":image})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})

def filter_by_location (request,location_id):
    title='Location'
    location =Location.object.all()
    image= Image.filter_by_location(id=location_id)

    return render(request, 'location.html',{"image":image,"location":location_id})
