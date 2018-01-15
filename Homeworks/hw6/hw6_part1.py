# File: hw6_part1.py
# Author: Ujjwal Rehani
# Date: 4/27/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Checks if a given word is a palindrome or not

# reverse() prints out a word in reverse
# Input: word; a word the user would like to reverse
# Output: palindrome; word after is has been reversed
def reverse(word):
	#Return empty string if word is empty
	if word == "":
		return word
	else:
		palindrome = reverse(word[1:]) + word[0]
		return palindrome
	
def main():
	userWord = input("Please enter a word to check for palindrome-ness: ")
	palindrome = reverse(userWord)
	
	#converts both string to lowercase for case insensitivity
	lowerWord = userWord.lower()
	lowerPalindrome = palindrome.lower()
	
	#compares the original string and reverse string
	if(lowerPalindrome == lowerWord):
		print("The word",userWord,"IS a palindrome")
	else:
		print("Sorry, the word",userWord,"is NOT a palindrome.")
		print("Backwards, it becomes",palindrome +".")

main()