# import fan class
from FanClass import Fan

# First object, assign the maximum speed, radius 10, color yellow, and turn it on
fan1 = Fan()
fan1.set_speedFAST()
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_fanON()
# Display first object speed, radius, color, on properties
print(f"Speed: {fan1.get_speed()} \nRadius: {fan1.get_radius()} \nColor: {fan1.get_color()} \nOn: {fan1.get_on()}\n")

# Second object, assign the medium speed, radius 5, color blue, and turn it off
fan2 = Fan()
fan2.set_speedMEDIUM()
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_fanOFF()
# Dsiplay second object speed, radius, color, on properties
