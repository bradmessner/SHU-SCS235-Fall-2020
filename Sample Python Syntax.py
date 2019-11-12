"""
Title:    Sample Python Syntax
Author:   Brad D. Messner
Date:     October 29, 2019
Version:  1.0
"""
# Hash signs (pound or number signs) are used to designate comments

# The print statement can be used to output basic comments to the console
# Note that there is no required terminal punctuation such as a semicolon as in Java
print("Hello.  This is your introduction to Python.")
print("You can output basic text in this manner.")

# You can use if and elif for basic decisions structures
# Note that a paranthesis is optional but the colon at the end is required
# Unlike Java, any statement indented afterwards is linked to the if statement
if 10 < 2:
    print("10 is not less than 2")
    print("Conversely, 2 is not greater than 10")
else:
    print("2 is less than 10")

# Python does NOT require the declaration of specific variables by type
# These would be consdisered global variables and available to any function
age = 25  # This will declare an integer
name = 2  # This will declare an integer
print (age + name)
name = "Brad"  # This will not consider name to be a string
print("My name is " + name + ".")
firstName, middleName, lastName = "Brad", "D", "Messner"  # This will assign multiple variables at the same time
fullName = ["Brad", "D", "Messner"]  # This will create an array of strings
print(fullName[0] + " " + fullName[1] + " " + fullName[2])
print("Your full name has " + str(len(fullName)) + " parts.")

# However, you can force an automatic variable type through declaration
speed = float(65.0)
speed2 = int(66)

# You will need to use a function if you wish to combine a a numeric and string output
print(name + " is " + str(age) + " years old.")

# If you need to use a random number
import random  # This should be at the beginning of the file

randomNumber = random.randrange(1, 100)
print("Your random number is: " + str(randomNumber))

# Basic loop structures work as in many other modern languages
for x in fullName:
    print(x)

for x in range(1, 7):
    print("Number X is " + str(x))

y = 0
while y > 10:
    print("Number Y is " + str(y))
    y += 1


# You can create functions to utilize over and over again
# Note the separate by two lines
def calculate(s, t):
    print("The total is " + str(s * t))


# Now that my function is created, I can call it and pass in values
calculate(10, 16)

