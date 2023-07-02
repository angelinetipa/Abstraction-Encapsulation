# import pet class
from PetClass import Pet
from colorama import Style, Fore

# creates an object of the class and prompts the user to enter the name, type, and age of his or her pet
pet_name, pet_animal, pet_age = input(f"""\n(Add space between your answer){Style.BRIGHT}
Enter your pet's name, type and age: {Style.RESET_ALL}""").split()
users_pet = Pet(pet_name.capitalize(), pet_animal.capitalize(), pet_age)

# retrieve the pet’s name, type, and age and display this data on the screen
print(f"""{Style.BRIGHT}\nUSER'S PET INFORMATION {Style.RESET_ALL} {Style.BRIGHT}
▪ Name: {Fore.BLACK} {users_pet.get_name()} {Style.RESET_ALL} {Style.BRIGHT}
▪ Type of Animal: {Fore.BLACK} {users_pet.get_animal_type()} {Style.RESET_ALL} {Style.BRIGHT}
▪ Age: {Fore.BLACK} {users_pet.get_age()}\n{Style.RESET_ALL}""")