# File: hw4_part3.py
# Author: Ujjwal Rehani
# Date: 3/2/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Adds items and their quantites to a list

def main():

	itemList = []
	numList = []
	count = 0
	item = input("Please enter an item ('STOP' to quit): ")
	
	#Items are added to the list until sentinel value is typed in
	while(item != "STOP"):
		itemList.append(item)
		itemNum = int(input("Please enter the quantity you want to purchase: "))
		numList.append(itemNum)
		item = input("Please enter an item ('STOP' to quit): ")
	
	#Length of both lists are the same so only one counter is needed
	print("Here is your shopping checklist: ")
	while(count < len(itemList)):
		print(itemList[count],"   ","(",numList[count],")")
		count+=1


main()