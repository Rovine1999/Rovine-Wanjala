from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
    
    def __str__(self):
        return str(self.name)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
    
    


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name = value)

    


class Image(models.Model):
    # image = models.ImageField(blank=True, null=True,upload_to='photos/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    image = CloudinaryField('images')

    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()


    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(name = value)

    @classmethod
    def filter_by_location(cls, location):
        image_location = cls.objects.filter(location__name=location).all()
        return image_location

    class Meta:
        ordering = ['name']    
    
