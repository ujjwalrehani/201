# File: hw6_part3.py
# Author: Ujjwal Rehani
# Date: 4/27/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Generates the levels of Pascal's triangle


# pascal() uses recursion to create each level of Pascal's
# 		   triangle, reaching the requested height
# Input: currLevel; an int, the current level being created
# 		 levelsToMake; an int, the number of levels requested
# 		 levelList; a 2D list of ints, containing the levels
# Output: None; (levelList is changed in place, and the updated
# 				 levelList will be the same in main() )

def pascal(currLevel,levelsToMake,levelList):
	if levelsToMake == 1:
		return [[1]]
	else:
		currRow = [1]
		levelList = pascal(0,levelsToMake-1,0)
		topRow = levelList[-1]
		for currLevel in range(len(topRow)-1):
			#Adds the numbers from top row
			currRow.append(topRow[currLevel] + topRow[currLevel+1])
		currRow += [1]
		
		levelList.append(currRow)
	return levelList
	
		
			
		
def main():
	print("Welcome to the Pascal's triangle generator.")
	levels = int(input("Please enter the number of levels to generate: "))
	#Checks for valid number
	while(levels < 1):
		print("Your number must be positive (greater than zero).")
		levels = int(input("Please enter the number of levels to generate: "))
	
	pascalList = [[1]]
	currentLevel = 0
	triangle = pascal(currentLevel,levels+1,pascalList)
	
	#prints out the triangle
	for row in triangle:
		print()
		for element in row:
			print("",element,end="")

main()

