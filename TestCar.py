# import car class
from CarClass import Car
from colorama import Style, Fore

# creates a Car object
my_car = Car(2021, "Honda Civic Hatchback")
# calls the accelerate method five times
for number in range(5):
    my_car.accelerate()
    # get the current speed of the car and display it
    print(f"""{Style.BRIGHT}\n{my_car.get_make()} {my_car.get_year()} {Style.RESET_ALL} {Fore.BLACK}>>  Accelerated by {number + 1} times {Style.RESET_ALL}
{Style.BRIGHT}▪ Speed: {Style.RESET_ALL}{my_car.get_speed()}""")
    
# call the brake method five times
for number in range(6):
    my_car.brake()
    # get the current speed of the car and display it
    print(f"""{Style.BRIGHT}\n{my_car.get_make()} {my_car.get_year()} {Style.RESET_ALL} {Fore.BLACK}>>  Decelerated by {number + 1} times {Style.RESET_ALL}
{Style.BRIGHT}▪ Speed: {Style.RESET_ALL}{my_car.get_speed()}""")