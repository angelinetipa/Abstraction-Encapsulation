# import pet class
from PetClass import Pet
from colorama import Style, Fore

# creates an object of the class and prompts the user to enter the name, type, and age of his or her pet
pet_name, pet_animal, pet_age = input("(Add space between them.)\nEnter your pet's name, type and age: ").split()
users_pet = Pet(pet_name.capitalize(), pet_animal.capitalize(), pet_age)

# retrieve the pet’s name, type, and age and display this data on the screen
print(f"""{Style.BRIGHT}\nUSER'S PET INFORMATION {Style.RESET_ALL} {Style.BRIGHT}
▪ Name: {Style.RESET_ALL}{users_pet.get_name()} {Style.BRIGHT}
▪ Type of Animal: {Style.RESET_ALL}{users_pet.get_animal_type()} {Style.BRIGHT}
▪ Age: {Style.RESET_ALL}{users_pet.get_age()}\n""")