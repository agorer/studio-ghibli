from django.urls import path
from movies.list.views import movie_list_page
from movies.characters.views import characters_page

app_name = 'movies'

urlpatterns = [
    path('', movie_list_page, name='movie_list'),
    path('/<str:movie_id>/characters', characters_page)
]
