# File: hw4_part2.py
# Author: Ujjwal Rehani
# Date: 3/2/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Checks if the user has entered a password that satisfies all the conditions

MIN_LEN = 8
MAX_LEN = 20
NEED_CHAR = "!"

def main():

	
	passwordValid = False
	
	while(passwordValid == False):
		password = input("Please enter a password: ")
		passwordValid = True
		checkLower = password.lower()
		
		
		#Checks for correct length
		if len(password) < MIN_LEN:
			print("Your password is too short. Must contain atleast 8 characters")
			passwordValid = False
		#Checks for correct length
		if len(password) > MAX_LEN:
			print("Your password is too long. Must be no more than 20 characters")
			passwordValid = False
		
		count = 0
		#Checks if password is all lowercase
		if (checkLower == password):
			print("The password is all lowercase, so it must contain the character ! to be secure.")
			#Checks size of password again
			if len(password) < MIN_LEN:
				print("The password is all lowercase, so it must contain the character ! to be secure.")
			elif len(password) > MAX_LEN:
				print("The password is all lowercase, so it must contain the character ! to be secure.")
			else:
				while (count < len(password)):
					#If the password contains a exclaimation point, make it valid
					if(password[count] == NEED_CHAR):
						passwordValid = True
						count = len(password)
						
					#If the password does not have exclaimation point, reprompt user
					elif (password[count] != NEED_CHAR):
						passwordValid = False
						
					#print("The password is all lowercase, so it must contain the character ! to be secure.")
					count+=1
			
			
	print("Thanks for picking the super-secure password", password)


main()