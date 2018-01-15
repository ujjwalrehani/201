# File: hw3_part1.py
# Author: Ujjwal Rehani
# Date: 2/23/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Prints out Happy Birthday message for an acceptable age range



def main():

	age = int(input("Please enter your age: "))
	
	#while loop only executes if age is not within acceptable range
	while(age < 0 or age > 125):
		if (age > 125):
			print("An age of",age,"is not possible.")
			print("No one has lived for more than 125 years.")
			age = int(input("Please enter your age: "))
		elif (age < 0):
			print("An age of",age,"is not possible.")
			print("It's impossible to be negative years old.")
			age = int(input("Please enter your age: "))
	
	print("Happy",age,"th birthday!")


main()