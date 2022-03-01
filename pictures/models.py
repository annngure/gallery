from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.

class Photographer(models.Model):
    first_name =models.CharField(max_length =30 )
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(blank = True)


    def __str__(self):
        return self.first_name
    
    def save_Photographer(self):
        self.save()

    def delete_Photographer(self):
        self.delete()


    @classmethod
    def update_photographer(cls,id):
        cls.objects.filter(id=id).update(name=name)
    
    @classmethod
    def all_photographer(cls):
        photographer=Photographer.objects.all()
        return photographer

class Meta:
        odering = ['first_name']


class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    

    @classmethod
    def all_locations(cls):
        location=Location.objects.all()
        return location
    
    @classmethod   
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name


class Category(models.Model):
    name= models.CharField(max_length = 30)

    def save_Category(self):
        self.save()

    def delete_Category(self):
        self.delete()

    
    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id=id).update(name=name)

    @classmethod
    def all_category(cls):
        category=Category.objects.all()
        return category

    def __str__(self):
        return self.name

class Image(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length = 30)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    description= models.TextField(max_length = 300)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True )
    

    def save_Image(self):
        self.save()

    def delete_Image(self):
        self.delete()

    @classmethod
    def get_image_by_title(cls,title):
        image = Image.objects.get(title=title)
        return image

    @classmethod
    def update_image(cls, id ,image, description , name,category,location):
        cls.objects.filter(id = id).update(image=image,description=description,name=name,category=category,location=location)
    
    @classmethod
    def search_image(cls,category):
        image = cls.object.filter(category__name__icontains=search_category)   
        return image


