# File: hw4_part4.py
# Author: Ujjwal Rehani
# Date: 3/2/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Checks if subjects entered contain the string 'ology' at the end

NUM_SUBJECTS = 10

def main():
	
	subjectList = []
	count = 0
	
	#subjects are added until sentinel value of 10 subjects is reached
	while(count < NUM_SUBJECTS):
		subject = input("Please enter a subject to study: ")
		subjectList.append(subject)
		count +=1
	
	count2 = 0
	while(count2 < len(subjectList)):
		newSubject = subjectList[count2]
		#Checks the last 5 characters for 'ology'
		if(newSubject[-5:] == "ology"):
			print("You can study",newSubject)
			count2+=1
		else:
			print(newSubject,"is not real!")
			count2+=1


main()