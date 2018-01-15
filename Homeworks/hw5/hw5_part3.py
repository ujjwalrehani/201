# File: hw5_part3.py
# Author: Ujjwal Rehani
# Date: 4/6/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Store items in a grocery list and count how many items are in list

STOP = "STOP"
GROUPS = 4

# addItems() adds items to the list based on food group
# Input: listFood, a list that will be changed
# Output: newList ; a list with added items
def addItems(listFood):
	item = input("What would you like to buy? Enter 'STOP' to quit: ")
	
	while(item != STOP):
		print("Please select the food group that bread belongs to")
		print("The food groups are: ")
		print("0 - Veggie \n1 - Fruit \n2 - Protein \n3 - Grain \n4 - Dairy")
		
		foodGroup = int(input("Enter a number between 0 and 4 (inclusive):"))
		#check for correct input
		while(foodGroup < 0 or foodGroup > GROUPS):
			print("That number is not allowed. Please try again!")
			foodGroup = int(input("Enter a number between 0 and 4 (inclusive):"))
			
		listFood[foodGroup].append(item)
		item = input("What would you like to buy? Enter 'STOP' to quit: ")
	
	newList = listFood
	return newList


# printList() Prints out the items and number of items in each group
# Input: listFood, a 2d list containing items
# Output: none ; print statement
def printList(listFood):
	count = 0
	
	#Check the lists in each row
	while(count<len(listFood)):
		count2 = 1
		print("You are buying",len(listFood[count])-1,"",listFood[count][0],"items: ")
		
		#Only if list has items, print out items
		if(len(listFood[count])> 1):
			#Go thorugh each column and print out items
			while(count2<len(listFood[count])):
				print("\t",listFood[count][count2])
				count2+=1
		count +=1

def main():
	print("Welcome! This program allows you to create a grocery list")
	#initial list
	foodList = [["Veggie"], ["Fruit"], ["Protein"], ["Grain"], ["Dairy"]]
	
	#function calls to add items to list and print them
	filledList = addItems(foodList)
	printList(filledList)
	
main()