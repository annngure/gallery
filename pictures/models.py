from django.db import models
import datetime as dt

# Create your models here.

class Photographer(models.Model):
    first_name =models.CharField(max_length =30 )
    last_name = models.CharField(max_length= 30)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.first_name
    
    def save_Photographer(self):
        self.save()

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
    def update_location(cls,id):
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
    def search_by_title(cls,search_term):
        category = cls.object.filter(name__icontains=search_term)   
        return pictures

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to ='image/')
    title = models.CharField(max_length = 30)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    description= models.TextField(max_length = 30)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add = True ,null = True)
    

    def save_Image(self):
        self.save()

    def delete_Image(self):
        self.delete()

    @classmethod
    def get_image_by_title(cls,title):
        image = Image.objects.get(title=title)
        return image

   

