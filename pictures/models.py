from django.db import models

# Create your models here.

class Photographer(models.Model):
    first_name =models.CharField(max_length =30 )
    last_name = models.CharField(max_length= 30)
    email = models.EmailField()

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




