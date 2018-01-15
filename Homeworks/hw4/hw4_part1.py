# File: hw4_part1.py
# Author: Ujjwal Rehani
# Date: 3/2/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Adds items to a "to do" list and prints it out

def main():
	
	itemList = []
	count = 0
	item = input("Please enter an item (QUIT to quit): ")
	
	#Items are added to the list until sentinel value is typed in
	while(item != "QUIT"):
		itemList.append(item)
		item = input("Please enter an item (QUIT to quit): ")
	
	#Prints out items in the list until the counter equals length
	print("Here is your to do list: ")
	while(count < len(itemList)):
		print("[ ]",itemList[count])
		count+=1
	

main()