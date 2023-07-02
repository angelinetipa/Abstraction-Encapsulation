# class named Pet
class Pet:
    # _ _init_ _ method that creates these attributes (name, animal type, age)
    def __init__(self, name, animal, age):
        # _ _name (for the name of a pet)
        self.__name = name
        # _ _animal_type (for the type of animal that a pet is)
        self.__animal_type = animal
        # _ _age (for the pet’s age)
        self.__age = age

    # set_name() method assigns a value to the _ _name field
    def set_name(self, name):
        self.__name = name
    # set_animal_type() method assigns a value to the _ _animal_type field
    # set_age() method assigns a value to the _ _age field
    # get_name() method returns the value of the _ _ name field
    # get_animal_type() method returns the value of the _ _animal_type field
    # get_age() method returns the value of the _ _age field




