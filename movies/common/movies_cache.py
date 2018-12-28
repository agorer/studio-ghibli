from django.core.cache import cache


def cache_movies(movies):
    cache.set('__movies', movies)


def get_cached_movies():
    return cache.get('__movies')


def movies_are_cached():
    return cache.get('__movies') is not None


def cache_characters(movie_id, characters):
    cache.set(movie_id, characters)


def get_cached_characters(movie_id):
    return cache.get(movie_id)


def characters_are_cached(movie_id):
    return cache.get(movie_id) is not None
