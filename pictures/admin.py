from django.contrib import admin
from .models import Photographer, Location, Category

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Location)
admin.site.register(Category)