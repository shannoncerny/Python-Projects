# creates a class
def __init__(animal, name, owner, species, age): #initializes the attributes of class
        animal.name = name
        animal.owner = owner
        animal.species = species
        animal.age = age
        New_animal = Animal("Goose", "Shannon","Cat", 5)

    # creates classes with arguments
class Animal: # creates class Animal
    name = 'Goose'
    owner = 'Shannon'
    species = 'cat'
    age = 5
class Diet(Animal): # creates class diet that refers to class Animal
        morning_food = '1/3 can dry food'
        evening_food = '1/2 cup wet food'
class Exercise(Animal): # creates class exercise that refers to class Animal
        morning_exercise = 'Play with banana kick toy'
        evening_exercise = 'Chase around house'

