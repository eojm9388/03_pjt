from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/01-home.html')


def community(request):
    return render(request, 'movies/02-community.html')