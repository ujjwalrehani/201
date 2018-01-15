# File: hw5_part2.py
# Author: Ujjwal Rehani
# Date: 4/6/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Checks if a name give by a user is a common name based on its ending

# isProperName() check if name is all lowercase, with an uppercase first letter
# Input: name, a string that will be checked
# Output: boolean ; true if name is all lowercase, with an uppercase first letter
#				or false if not
def isProperName(name):
	
	#splices the string so one letter into one string and rest into another 
	firstLet = name[0]
	restLet = name[1:]
	
	#checks if it is proper name
	if(firstLet == firstLet.upper() and restLet == restLet.lower()):
		return True
	else:
		return False
	

# isSameEnd() checks if fullString ends with endString (case sensitive)
# Input: fullString; string name
# 		 endString; ending from list of common endings
# Output: boolean; true if fullString ends with endString or false if not
def isSameEnd(fullString,endString):
	#gets the length of the common ending
	lenEnd = len(endString)
	
	#splices the ending from the name and compares the endings
	spliceEnd = fullString[-lenEnd:]
	if endString == spliceEnd:
		return True
	else:
		return False
	print()


# checkCommonEndings() check if name ends in any of the common endings
# Input: name; 
# 		 commonEndings; list of strings
# Output: firstCom; the first common ending found in name
def checkCommonEndings(name,commonEndings):
	bool = False 
	count = 0
	
	#Checks each ending and break out of loop once first ending matches
	while(count < len(commonEndings) and bool == False):
		if(isSameEnd(name,commonEndings[count]) == True):
			bool = True
		count += 1
	
	#Determine if name has common ending or not
	if bool == True:
		firstCom = commonEndings[count-1]
		print("Your name is common, since it ends in",commonEndings[count-1])
		return firstCom
	else:
		print("Your name is uncommon! Congratulations!")
		firstCom = ""
		return firstCom


def main():
	commonEndings = ["son", "stern", "man", "in", "er", "en", "el","on"]
	print("Welcome! This program checks if your name is common.")
	userName = input("Please enter your name: ")
	
	#Checks for proper name 
	while(isProperName(userName) == False):
		print("Sorry, but a proper name starts with a capital letter.")
		userName = input("Please enter your name: ")
	
	#Calls function to determine whether name has common ending
	checkCommonEndings(userName,commonEndings)
	
	print("Thank you for using the common name checker!")

main()