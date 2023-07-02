# import pet class
from PetClass import Pet
from colorama import Style, Fore

# creates an object of the class and prompts the user to enter the name, type, and age of his or her pet
pet_name, pet_animal, pet_age = input("(Put comma between them.)\nEnter your pet's name, type and age: ")
users_pet = Pet(pet_name, pet_animal, pet_age)
# retrieve the pet’s name, type, and age and display this data on the screen