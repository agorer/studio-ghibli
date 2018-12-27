from .character import Character


def parse(apiMovie):
    return Character(apiMovie['id'],
                     apiMovie['name'],
                     apiMovie['gender'])
