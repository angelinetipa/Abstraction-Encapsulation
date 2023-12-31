# import fan class
from FanClass import Fan
from colorama import Style

# First object, assign the maximum speed, radius 10, color yellow, and turn it on
fan1 = Fan()
fan1.set_speedFAST()
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.set_fanON()
# Display first object speed, radius, color, on properties
print(f"""{Style.BRIGHT}\nFIRST FAN\n▪ Speed:  {Style.RESET_ALL}{fan1.get_speed()} 
{Style.BRIGHT}▪ Radius: {Style.RESET_ALL}{fan1.get_radius()} 
{Style.BRIGHT}▪ Color:  {Style.RESET_ALL}{fan1.get_color()} 
{Style.BRIGHT}▪ On:     {Style.RESET_ALL}{fan1.get_on()}""")

# Second object, assign the medium speed, radius 5, color blue, and turn it off
fan2 = Fan()
fan2.set_speedMEDIUM()
fan2.set_radius(5)
fan2.set_color("blue")
fan2.set_fanOFF()
# Dsiplay second object speed, radius, color, on properties
print(f"""{Style.BRIGHT}\nSECOND FAN\n▪ Speed:  {Style.RESET_ALL}{fan2.get_speed()} 
{Style.BRIGHT}▪ Radius: {Style.RESET_ALL}{fan2.get_radius()} 
{Style.BRIGHT}▪ Color:  {Style.RESET_ALL}{fan2.get_color()} 
{Style.BRIGHT}▪ On:     {Style.RESET_ALL}{fan2.get_on()}\n""")