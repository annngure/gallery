from django.contrib import admin
from .models import Photographer, Location, Category ,Image

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)