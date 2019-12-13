from django.shortcuts import render

.
def photos(request):
    return  render(request, 'photo.html')
def search_results(request):
    search = dt.image.get()
    return render(request, 'all-images/search.html')

