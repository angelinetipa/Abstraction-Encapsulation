# class named Car
class Car:
    # constructor that accepts the car’s year model, make as arguments, assign 0 to the speed 
    def __init__(self, year, make, speed = 0):
        # _ _year_model (for the car’s year model)
        self.__year_model = year
        # _ _make (for the make of the car)
        self.__make = make
        # _ _speed (for the car’s current speed)
        self.__speed = speed
# accelerate method should add 5 to the speed data attribute each time it is called
# brake method should subtract 5 from the speed data attribute each time it is called
# get_speed method should return the current speed