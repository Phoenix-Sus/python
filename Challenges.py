### Triangular numbers ###
# continuous summation of consecutive numbers #
# print("Size of list")
# size = int(input())
# print("-------------------")
# print("Here's the list:")
# temp = 0
# count = 1

# while(count <= size):
#     temp = temp + count
#     print(temp)
#     count = count+1

### EXTRA STUFF WITH STRINGS ###
# word = "Ethan Susanto"
# word = word.split(" ") # uses the space as a delimiter
# print(word[0])
# print(word[1])


### Program which outputs prime numbers ###
# print("Give us a number bruh: ")
# size = int(input())
# print("---------------------")
# currentNum = 1
# temp = 1
# count = 0
# flag = False

# while (count < size):
#     if (currentNum == 1):
#         print(str(currentNum) + ", ")
#         count = count + 1
#     elif (currentNum > 1):
#         # check for factors #
#         for temp in range(2, currentNum):
#             if (currentNum % temp) == 0:
#                 # If zero factor is found, hence, not prime
#                 flag = True
#                 break

#         # If number is prime
#         if (flag == False):
#             print(str(currentNum) + ", ")
#             count = count + 1

#     currentNum = currentNum + 1

#     # Reset flag
#     flag = False


### SIMULATE PROJECTILE MOTION ###
# print("Please enter initial x velocity")
# xVel = int(input())
# print("Now enter an initial y velocity")
# yVel = int(input())
# xDis = 0
# yDis = 0
# gravity = 9.81

# # Firstly find time of flight
# tof = 2 * ( (yVel - 0)/gravity )

# # Calculate distance along straight path #
# xDis = xVel * tof

# # Print results #
# print("Travelled {:.2f}m in {:.2f} seconds".format(xDis, tof))



### Write a program to tell the current system time ###
import datetime

# Get current date and time
print(datetime.datetime.now())

# get different parts of it?
print("Hour: {:.2f}".format(datetime.hour))