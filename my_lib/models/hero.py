from .hero_def import Hero


def get_name(hero: Hero) -> str:
    """Returns name

    >>> get_name(Hero(name="Deadpond", secret_name="Dive Wilson"))
    'Deadpond'
    """
    return hero.name