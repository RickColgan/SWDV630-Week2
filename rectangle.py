# This program will calculate the area of a rectangle by applying a method to a rectangle object
# I only commented each line because I wanted you to know that I am capable but don't always do it

class Rectangle():
    def __init__(self, height, width):  # constructor
        self.height = height  # assign the height entered by the user to the Rectangle object
        self.width = width    # assign the width entered by the user to the object

    def area(self):           # define the area method for the Rectangle object
        return self.height * self.width    # formula for area per Geometry 101

# main program starts here
# I didn't know your preferences on using a main() function
# I will do it on bigger projects, but little ones like this, it just seems like a waste

# Get height of rectangle
h = int(input("Enter the height of the rectangle: "))

# Get width of rectangle
w = int(input("Enter the width of the rectangle: "))

# Initialize an object of the Rectangle class
obj = Rectangle(h, w)

# get the area per the assignment
print("Area of the rectangle is: ", obj.area())

print()