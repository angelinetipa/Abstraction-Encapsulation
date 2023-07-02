# class named fan
class Fan:
    # constants named SLOW with value 1
    SLOW = 1
    # constants named MEDIUM with value 2
    MEDIUM = 2
    # constants named FAST with value 3
    FAST = 3

    # constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False)
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False ):
        # private int data field named speed 
        self.__speed = speed
        # private float data field named radius 
        self.__radius = radius
        # private string data field named color
        self.__color = color 
        # private bool data field named on
        self.__on = on

    # getter methods
    def get_speed(self):
        return self.__speed
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    def get_on(self):
        return self.__on
    
    # setter methods
    def set_speed(self, speed):
        self.__speed = speed