from .character import Character


def parse(apiCharacter):
    return Character(apiCharacter['id'],
                     apiCharacter['name'],
                     apiCharacter['gender'])
