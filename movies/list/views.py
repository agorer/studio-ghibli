from django.shortcuts import render
from movies.common.movies_repository import MoviesRepository


def movie_list_page(request):
    repository = MoviesRepository()

    context = {
        'movies': repository.find_all()
    }

    return render(request, 'movies/list/movie_list.html', context)
