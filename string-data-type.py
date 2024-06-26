#!/usr/bin/python3
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdstring = firstString + secondString
print(thirdstring)
#working with inputs
name = input("What is your name? ")
print(name)
#formatting output strings
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))