# class named Car
class Car:
    # constructor that accepts the car’s year model, make as arguments, assign 0 to the speed 
    def __init__(self, year, make):
        # _ _year_model (for the car’s year model)
        self.__year_model = year
        # _ _make (for the make of the car)
        self.__make = make
        # _ _speed (for the car’s current speed)
        self.__speed = 0

    # accelerate method should add 5 to the speed data attribute each time it is called
    def accelerate(self):
        self.__speed += 5
      
    # brake method should subtract 5 from the speed data attribute each time it is called
    def brake(self):
        self.__speed -= 5

    # get_speed method should return the current speed
    def get_speed(self):
        return self.__speed