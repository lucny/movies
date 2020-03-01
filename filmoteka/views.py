from django.shortcuts import render
from .models import Film

def film_list(request):
    films = Film.objects.all()
    return render(request, 'filmoteka/film_list.html', {'films': films})
