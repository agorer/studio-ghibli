from .movie import Movie


def parse(jsonMovie):
    return Movie(jsonMovie['id'],
                 jsonMovie['title'],
                 jsonMovie['description'],
                 int(jsonMovie['release_date']))
