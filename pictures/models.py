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

    def save_Location(self):
        self.save()

    def delete_Location(self):
        self.delete()


class Category(models.Model):
    name= models.CharField(max_length = 30)

    def save_Category(self):
        self.save()

    def delete_Category(self):
        self.delete()

    @classmethod
    def search_

class Image(models.Model):
    picture = models.ImageField(upload_to ='images/')
    title = models.CharField(max_length = 30)
    photographer = models.ForeignKey(Photographer)
    description= models.StringField(max_length = 30)
    location= model.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add = True ,null = True)
    




