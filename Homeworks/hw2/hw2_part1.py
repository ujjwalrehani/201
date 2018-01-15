# File: hw2_part1.py
# Author: Ujjwal Rehani
# Date: 2/15/2017
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Asks the user for a grade and prints out a corresponding message

def main():

	className = input("Please enter the name of the class: ")
	classGrade = input("Please enter your letter classGrade: ")
	
	if(classGrade == "A" or classGrade == "B" or classGrade == "C" or classGrade == "D"):
		print("You passed",className)
	elif(classGrade == "F"):
		print("You failed",className)
	elif(classGrade == "W"):
		print("You withdrew from",className)
	else:
		print(classGrade,"is not a valid classGrade for",className)

main()