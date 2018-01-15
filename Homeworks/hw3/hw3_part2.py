# File: hw3_part2.py
# Author: Ujjwal Rehani
# Date: 2/23/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Performs integer division without using  integer division, 
#   “regular” division, or modulus.




def main():

	firstNum = int(input("Please enter the first number: "))
	#input validation for first and second numbers
	while (firstNum < 0):
		firstNum = int(input("Please enter the first number: "))
	secondNum = int(input("Please enter the second number: "))
	while (secondNum < 1):
		secondNum = int(input("Please enter the second number: "))
		
	dividend = firstNum
	count = 0
	
	if (firstNum == 0 or firstNum < secondNum):
		print(firstNum," // ",secondNum ,"=", "0")
		
	elif (firstNum == secondNum):
		print(firstNum," // ",secondNum ,"=", "1")
			
	else:
		while (dividend > 0):
			#Subtracts the divisior from the dividend until dividend reaches 0
			dividend = dividend - secondNum
			#counts the number of subtractions taken place
			count += 1
			
			if(dividend < secondNum):
				#stops while loop if dividend becomes negative
				dividend = 0
			
		print(firstNum," // ",secondNum ,"=", count)
	

main()