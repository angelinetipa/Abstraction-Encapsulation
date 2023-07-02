# Abstraction-Encapsulation
## FAN CLASS
### First Program
Design a class named Fan to represent a fan. The class contains:
- Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
- A private int data field named speed that specifies the speed of the fan.
- A private bool data field named on that specifies whether the fan is on (the default is False).
- A private float data field named radius that specifies the radius of the fan.
- A private string data field named color that specifies the color of the fan.
- The accessor(getters)  and mutator(setters)  methods for all four data fields.
- A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
  
### Second Program
- Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
- Assign medium speed, radius 5, color blue, and turn it off for the second object.
- Display each object’s speed, radius, color, and on properties.


## CAR CLASS
###  First Program
- Write a class named Car that has the following data attributes:
```
 _ _year_model (for the car’s year model)
 _ _make (for the make of the car)
 _ _speed (for the car’s current speed)
```
- The Car class should have an _ _init_ _ method that accepts the car’s year model and make as arguments. These values should be assigned to the object’s _ _year_model and _ _make data attributes. It should also assign 0 to the _ _speed data attribute.
- The class should also have the following methods:
accelerate(). The accelerate method should add 5 to the speed data attribute each time it is called.
brake(). The brake method should subtract 5 from the speed data attribute each time it is called.
get_speed(). The get_speed method should return the current speed.

### Second Program
- Next, design a program that creates a Car object then calls the accelerate method five times.
- After each call to the accelerate method, get the current speed of the car and display it.
- Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.


## PET CLASS
###  First Program
- Write a class named Pet, which should have the following data attributes:
```
_ _name (for the name of a pet)
_ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
_ _age (for the pet’s age)
```
- The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
```
set_name(). This method assigns a value to the _ _name field.
set_animal_type(). This method assigns a value to the _ _animal_type field.
set_age(). This method assigns a value to the _ _age field.
get_name(). This method returns the value of the _ _ name field.
get_animal_type(). This method returns the value of the _ _animal_type field.
get_age(). This method returns the value of the _ _age field.
```

### Second Program
- Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet.
- This data should be stored as the object’s attributes.
- Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.









