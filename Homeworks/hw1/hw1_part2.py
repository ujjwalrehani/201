# File: hw1_part2.py
# Author: Ujjwal Rehani
# Date: 2/9/2017
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
#	Calculates the number of people wearing hats

def main():
	wearHats = float(input("How many people are wearing hats? "))
	noHats = float(input("How many people are not wearing hats? "))
	totalPeople = wearHats + noHats
	perHats= (wearHats/totalPeople) * 100
	
	print(perHats,"% of the people are wearing hats")
	


main()