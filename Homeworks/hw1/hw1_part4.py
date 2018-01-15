# File: hw1_part4.py
# Author: Ujjwal Rehani
# Date: 2/9/2017
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
#	Calculates and prints out the number of rooms in a castle 

def main():
	numFloors = int(input("How many floors are in the castle? "))
	numRooms = int(input("How many rooms are there on each floor? "))
	castleRooms = numFloors * numRooms
	
	print("There are",castleRooms,"in the castle")



main()