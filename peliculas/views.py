from django.shortcuts import render
from .models import Genre, Movie
# Create your views here.

def index(request):
    num_movies=Movie.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={'num_movies':num_movies},
    )

# Create your views here.
