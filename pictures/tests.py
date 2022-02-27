from django.test import TestCase
from .models import Photographer, Location, Category


# Create your tests here.

class PhotographerTestClass(TestCase):

    #set up method
    def setUp(self):
        self.ann=Photographer(first_name= 'Joses',last_name='Mwita',email='joses@gmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ann,Photographer))

    #Testing save method
    def test_save_method(self):
        self.ann.save_Photographer()
        photographer = Photographer.objects.all()
        self.assertTrue(len(photographer) > 0)