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
    post = models.TextField()
    Category = models.ForeignKey(Category)


class Location (models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location
        class Meta:
            ordering = ['location']

    
