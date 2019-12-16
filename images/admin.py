from django.contrib import admin
from .models import Category,Image


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):


    admin.site.register(Category)
    admin.site.register(Image)


