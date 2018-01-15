# File: hw2_part3.py
# Author: Ujjwal Rehani
# Date: 2/15/2017
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Asks the users questions about dogs and prints out the name
#	of the matching dog

def main():

	print("Please enter 'yes' or 'no' to these questions.")
	shortLegs = input("Does your dog have short legs? ")
	
	if (shortLegs == "yes"):
		longFur = input("Does your dog have long fur? ")
		if(longFur == "yes"):
			print("Your dog is a Shetland Sheepdog!")
		else:
			print("Your dog is a Swedish Vallhund!")
			
	elif (shortLegs == 'no'):
		bigDog = input("Is your dog a big dog? ")
		if(bigDog == "yes"):
			curlyTail = input("Does your dog have a curly tail? ")
			if(curlyTail == "yes"):
				print("Your dog is a Kangal!")
			if(curlyTail == "no"):
				print("Your dog is a Irish Wolfhound!")
		else:
			print("Your dog is a Azawakh!")

main()