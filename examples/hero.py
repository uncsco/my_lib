from my_lib.models import hero
from my_lib.models.hero import Hero


#// https://sqlmodel.tiangolo.com/#create-rows
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

print(hero.get_name(hero_1))
print(hero.get_name(hero_2))
print(hero.get_name(hero_3))