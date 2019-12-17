from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name
        class Meta:
            ordering = ['name']
    

class Image(models.Model):
    title = models.CharField(max_length =60)
    category_object = models.ForeignKey(Category)
    # location = models.ForeignKey(Location)
    photos_image = models.ImageField(upload_to = 'photos/')

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category_object__name__icontains=search_term)
        return gallery


class Location (models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location
        class Meta:
            ordering = ['location']

    
