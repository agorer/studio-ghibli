from django.urls import path
from movies.list import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list_page, name='movie_list')
]
