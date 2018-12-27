from django.shortcuts import render
from movies.list.movies_repository import MoviesRepository


def characters_page(request, movie_id):
    repository = MoviesRepository()

    context = {
        'characters': repository.find_characters(movie_id)
    }

    return render(request, 'movies/characters/characters.html', context)
