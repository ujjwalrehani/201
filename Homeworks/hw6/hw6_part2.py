# File: hw6_part2.py
# Author: Ujjwal Rehani
# Date: 4/27/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Calculates the greates common denominator of two numbers

# gcd() calculates the GCD of two numbers
# Input: num1, num2; two numbers that will checked for GCD
# Output: num2; the GCD of the initial two numbers
def gcd(num1,num2):
	if num2 > num1:
		return gcd(num2, num1)
	#find remainder
	mod = num1 % num2
	
	#Once remainder is zero,GCD has been found
	if mod == 0:
		return num2
	return gcd(mod, num2)



def main():

	firstNum = int(input("Please enter the first integer: "))
	#Checks for valid first value
	while(firstNum < 1):
		print("Number must be greater than zero.")
		firstNum = int(input("Please enter the first integer: "))
	
	secondNum = int(input("Please enter the second integer: "))
	#Checks for valid second value
	while(secondNum < 1):
		print("Number must be greater than zero.")
		secondNum = int(input("Please enter the second integer: "))
		
	answer = gcd(firstNum,secondNum)
	print("The GCD for",firstNum,"and",secondNum,"is",answer)
	
		
main()