# File: hw3_part4.py
# Author: Ujjwal Rehani
# Date: 2/23/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description: 
# 	Prints out a box where there are width numbers and height rows



def main():

	width = int(input("Please enter a width: "))
	#Input validation
	while(width < 1):
		width = int(input("Please enter a width: "))
	height = int(input("Please enter a height: "))
	while(height < 1):
		height = int(input("Please enter a height: "))
		
	maxNum = width * height
	count = 0
	
	while(count < maxNum):
		count += 1
		print(count,"",end="")
		#Last number of each row has remainder of zero when divided by width
		#Thus when remainder is 0, a new row begins
		if (count % width == 0):
			print("")
		
		
main()