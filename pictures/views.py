from django.shortcuts import render
from django.http import HttpResponse
from .models import Photographer, Location, Category
# Create your views here.

def index(request):
    return render(request,'index.html')