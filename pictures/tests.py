from django.test import TestCase
from .models import Photographer, Location, Category ,Image


# Create your tests here.

class PhotographerTestClass(TestCase):

    #set up method
    def setUp(self):
        self.ann=Photographer(first_name= 'Joses',last_name='Mwita',email='joses@gmail.com')
        self.ann.save_Photographer()
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ann,Photographer))

    #Testing save method
    def test_save_method(self):
        self.ann.save_Photographer()
        photographer = Photographer.objects.all()
        self.assertTrue(len(photographer) > 0)

class LocationTestClass(TestCase):

    #setUp
    def setUp(self):
        self.ann=Location(name= 'Kericho')
        self.ann.save_location
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ann,Location))

    #Testing save method
    def test_save_method(self):
        self.ann.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    #delete method
    def test_delete_method(self):
        self.ann.save_location()
        self.ann.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)
    #update method
    def test_update_location(self):
        changed_location = 'Asia'
        self.ann.update_location(self.location.id, changed_location)
        changed_location = Location.objects.filter(name='Asia')
        self.assertTrue(len(changed_location) == 1)


class CategoryTestClass(TestCase):

    #setUp
    def setUp(self):
        self.ann=Category(name= 'Food')
        self.ann.save_Category()
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ann,Category))

    #Testing save method
    def test_save_method(self):
        self.ann.save_Category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    #delete method
    def test_delete_method(self):
        self.ann.save_Category()
        self.ann.delete_Category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

    # Update method
    def test_update_category(self):
        changed_location = 'Fashion'
        self.category.update_category(self.category.id, changed_location)
        changed_location = Category.objects.filter(name='Fashion')
        self.assertTrue(len(changed_location) == 1)
    
    


  
class ImageTestClass(TestCase):

    #setUp
    def setUp(self):
        self.ann=Image(title= 'image',description='image')
        self.ann.save_Image()
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ann.Image))

    #Testing save method
    def test_save_method(self):
        self.ann.save_Image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    #delete method
    def test_delete_method(self):
        self.ann.save_Image()
        self.ann.delete_Image()
        image= Image.objects.all()
        self.assertTrue(len(image)==0)      