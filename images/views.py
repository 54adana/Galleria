from .models import  Location,Image,Category
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt


def photos(request):
    images = Image.get_images()
    return render(request,'photos.html', {'images':images})

def search_results(request):
    search = dt.image.get()
    return render(request, 'all-images/search.html')
    
def location(request):
    return render(request, 'photos.html')

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})