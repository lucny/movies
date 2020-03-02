from django.shortcuts import render, get_object_or_404
from .models import Film

def film_list(request):
    films = Film.objects.all()
    return render(request, 'filmoteka/film_list.html', {'films': films})

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'filmoteka/film_detail.html', {'film': film})