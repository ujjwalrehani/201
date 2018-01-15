# File: hw3_part3.py
# Author: Ujjwal Rehani
# Date: 2/23/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Prints out height of hailstorm



def main():

	height = int(input("Please enter the starting height of the hailstone: "))
	#Input validation
	while (height < 0):
		height = int(input("Please enter the starting height of the hailstone: "))
		
	while (height > 1):
		print("Hail is currently at height ",height)
		#Checks if odd or even
		if (height % 2 == 0):
			height = height // 2
		elif (height % 2 == 1):
			height *= 3
			height += 1
			
	if (height == 1):
		print("Hail stopped at height ",height)
	elif (height == 0):
		print("Hail stopped at height ",height)


main()
