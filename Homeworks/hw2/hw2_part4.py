# File: hw2_part4.py
# Author: Ujjwal Rehani
# Date: 2/15/2017
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Asks the user for a date and prints out the corresponding day
#	for February

def main():
	
	date = input("Please enter the day of the month: ")
	
	if (date == "5" or date == "12" or date == "19" or date == "26"):
		print("Today is a Sunday!")
	elif (date == "6" or date == "13" or date == "20" or date == "27"):
		print("Today is a Monday!")
	elif (date == "7" or date == "14" or date == "21" or date == "28"):
		print("Today is a Tuesday!")
	elif (date == "1" or date == "8" or date == "15" or date == "22"):
		print("Today is a Wednesday!")
	elif (date == "2" or date == "9" or date == "16" or date == "23"):
		print("Today is a Thursday!")
	elif (date == "3" or date == "10" or date == "17" or date == "24"):
		print("Today is a Friday!")
	elif (date == "4" or date == "11" or date == "18" or date == "25"):
		print("Today is a Saturday!")
	else:
		print("The date",date,"is an invalid day.")

main()