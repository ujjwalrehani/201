# File: hw2_part2.py
# Author: Ujjwal Rehani
# Date: 2/15/2017
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Asks the user number of seconds and calulates number 
#	of seconds in minutes,hours,and days

def main():

	numSeconds = int(input("Please enter a number of seconds: "))
	
	if (numSeconds < 0):
		print("Cannot calculate for a negative number")
		
	elif (numSeconds < 60):
		print("There are 0 minutes in",numSeconds,"seconds")
		print("There are 0 hours in",numSeconds,"seconds")
		print("There are 0 days in",numSeconds,"seconds")
		
	elif (numSeconds <3600):
		print("There are" ,numSeconds//60 ,"minutes in",numSeconds,"seconds")
		print("There are 0 hours in",numSeconds,"seconds")
		print("There are 0 days in",numSeconds,"seconds")
	
	else:
		print("There are",numSeconds//60,"minutes in",numSeconds,"seconds")
		print("There are",numSeconds//3600,"hours in",numSeconds,"seconds")
		print("There are",numSeconds//86400,"days in",numSeconds,"seconds")
		
	






main()