# This is a comment #
# Print the thing we are learning today #
# print("Today we gon learn some Python!") # No semicolons in python #

# # Print the combined ages of you and your brother
# EthanAge = 19
# SolomonAge = 17
# print(EthanAge+SolomonAge)

# # Do a more complex calculation #
# JudyAge = 20
# NoGuitars = 5
# TotalValue = (EthanAge + SolomonAge + JudyAge) * NoGuitars
# print("The number we got is: {}". format(TotalValue))  # Including variables in sentences is a bit different to C

# # Get the different types of variables #
# p = 5       # INTEGER
# print("P is of type: {}".format(type(p)))
# p = 2.5     # FLOAT
# print("P is of type: {}".format(type(p)))
# p = "sup"   # STRING
# print("P is of type: {}".format(type(p)))
# p = []      # LIST
# print("P is of type: {}".format(type(p)))

# Try some Additions!
# print(5 + 5)                  # DOES THE CALCULATION FOR YOU
# print("ETHAN" + " IS COOL")   # CONCATENATES THE GIVEN STRINGS
# print(5 + "hello")            # CANNOT COMBINE NUMBERS AND STRINGS
# print(2.0/5)                  # SEEMS YOU CAN COMBINE DIFFERENT NUMERICAL TYPES

# TYPECASTING IS A THING TOO
# print(str(5) + "Ethans")
# print(5 + int("5"))

### INPUTS ###
# prompt = "What's your name?"
# print(prompt)
# name = input()
# print("So your name is {} correct?".format(name))
# # print("So your name is " + name + " correct?") # Another way to write the above line 

# print("Let's sum up some numbers, so give me two! (integers please)")
# num1 = input()
# num2 = input()
# sum = int(num1) + int(num2)
# print("Bruv if you can't do that yourself...")
# print("Sigh, the answer is: {}".format(sum))


# ### CONTROLS ###
# print("What's your name?")
# name = input()
# print("Hey there " + name + ", Do you want to play? (yes/no)")
# answer = input()

# if (answer == "yes") :
#     print("Great, let's get started.")
#     print("Give me a number!")
#     num = int(input())

#     # COUNTDOWN SEQUENCE #
#     while (num > 0):
#         print(num)
#         num = num-1

#     print("YAY NOW WE FRIENDS!")
# else:
#     print("That's a shame, f**k off.")


# ### LISTS ###
# print("We gon use a list / array to get some numbers.")
# array = []  # Don't need to declare nuffin bruva
# arrayPTR = 1

# while (len(array) < 5):
#     if (arrayPTR == 1):
#         position = str(arrayPTR) + "st"
#     elif (arrayPTR == 2):
#         position = str(arrayPTR) + "nd"
#     elif (arrayPTR == 3):
#         position = str(arrayPTR) + "rd"
#     else:
#         position = str(arrayPTR) + "th"

#     print("Give me your " + position + " favourite number.")

#     # Add the input to the list #
#     array.append(input())
#     arrayPTR = arrayPTR + 1

# # Let's print in reverse order now #
# arrayPTR = len(array)
# while (arrayPTR > 0):
#     arrayPTR = arrayPTR - 1
#     print(array[arrayPTR])


### DICTIONARIES ##
# meaning = []
# size = []

# meaning["apple"] = "A fruit"    # Here meaning and size are dictionaries
# size["apple"] = 5               # APPLE is a key, which gives you the corresponding response from the dictionaries


### FUNCTIONS ###
# # Instead of 'function' we use 'def'
# def printNumbers(n):
#     temp = 0
#     stringOut = ""
#     while (temp<n):
#         stringOut = stringOut + str(temp) + " "
#         temp = temp+1

#     print(stringOut)

# # Print triangle
# print("Give size of triangle")
# size = int(input())
# temp = 0
# while (temp <= size):
#     printNumbers(temp)
#     temp = temp+1


### CLASSES ###
# Basically the equivalent of a structure #
# class cat:
#     def __init__(self):
#         self.size = 40
#         self.color = "blue"
#         self.breed = "persian"
#     def meow(self):
#         print("meow! I am a " + self.color + ", " + self.breed + " cat")

# molly = cat()
# jesse = cat()

# jesse.breed = "ocelot"

# molly.meow()
# jesse.meow()
    


# I Guess lets try some challenges #



