# File:    proj1.py
# Author:  Ujjwal Rehani
# Date:    3/9/2017 
# Section: 21
# E-mail:  urehani1@umbc.edu 
# Description:
#   This project classifies a list of numbers and prints out facts
#	about them

MIN_NUM = 1         # minimum number allowed
MAX_NUM = 100000    # maximum number allowed
ODD = "Odd"
EVEN = "Even"
PERF = "Perfect"    # return values for checkForPerfect function
ABD  = "Abundant"
DEF  = "Deficient"
TRI  = "Triangular"  # return values for isTriangular function
SQU = "Square"		 # return values for isSquare function
PRI = "Prime"		# return values for isPrime function
COM = "Composite"
NEI = "Neither"



# printGreeting() explains the program to the user
# Input:          none
# Output:         none (prints greeting)
def printGreeting():
	print("This program classifies positive integers as")
	print("Odd/Even, Prime/Composite, Perfect/Abundant/Deficient,")
	print("Square, and Triangular")
	print()
	print("You will now get to choose the range of positive integers that")
	print("you would like to see classified.")


# getValidInt() reprompts the user until they enter a number
#               between a minimum and maximum (inclusive)
# Input:        minn;   integer of lower accepted range
#               maxx;   integer of upper accepted range
# Output:       newInt; integer between minn and maxx inclusive
def getValidInt(minn,maxx):
	
	message = "Enter a number between " + str(minn) + " and " + \
        str(maxx) + " (inclusive): "
	
	newInt = int(input(message))
	#checks for valid input
	while(newInt < minn or newInt > maxx):
		print("That number is not allowed. Please try again!")
		message = "Enter a number between " + str(minn) + " and " + str(maxx) + " (inclusive): "
		newInt = int(input(message))
	return newInt

# printTableHead() prints heading of table
# Input:            none
# Output: 			none (print function)
def printTableHead():
	print("Int     Classifications....................................")
	print("-----------------------------------------------------------------------")

# isOdd() calculates whether num is odd or not
# Input:  num;      an integer we're checking for oddness
# Output: numIsOdd; a Boolean that says if num is odd or even
def isOdd(num):
	if(num % 2 == 0):
		num = False
	else:
		num = True
		
	numIsOdd = num
	return numIsOdd

# isPrime() calculates whether a number is prime or not
# Input:  num;      an integer we're checking if it is primeness
# Output: numIsPrime; a Boolean that says if num is prime or not
#                     (returns True if prime, False if not)
def isPrime(num):
	count = 2
	flag = 0
	
	#special case
	if num == 1:
		numIsPrime = NEI
		flag = 1
	while(count < num ):
		#checks what num can be divided by
		if(num % count == 0):
			flag = 1
			numIsPrime = False
		count +=1
	if flag == 0:
		numIsPrime = True
	
	return numIsPrime
			
# isSquare() calculates whether num is square or not
# Input:  num;      an integer we're checking for squareness
# Output: numIsSquare; a Boolean that says if num is square
def isSquare(num):
	root = num **.5
	if(num % root == 0):
		num = True
	else:
		num = False
	
	numIsSquare = num
	return numIsSquare

# isTriangular() calculates whether num is triangular or not
# Input:  num;      an integer we're checking for triangularness
# Output: numIsTri; a Boolean that says if num is triangular
#                   (returns True if triangular, False if not
def isTriangular(num):
	count = 0
	if(num == 1):
		numIsTri = True
		return numIsTri
	else:
		while(count < num):
			if((count * (count + 1) / 2) == num):
				numIsTri = True
				return numIsTri
			count+=1
			
		numIsTri = False
		return numIsTri
		
# checkForPerfect() calculates whether num is odd or not
# Input:  num;      an integer we're checking for perfectness
# Output: numIsPerf; string says whether a num is perfect, abundant or deficient
def checkForPerfect(num):
	if(num == sumDivisors(num)):
		numIsPerf = PERF
		return numIsPerf
	elif(num < sumDivisors(num)):
		numIsPerf = ABD
		return numIsPerf
	elif(num > sumDivisors(num)):
		numIsPerf = DEF
		return numIsPerf
		
# isDivisor() returns if one number is a divsor of another
# Input:  origNum, possDiv;  an integer we're checking if it is divisible or not
# Output: numIsDiv; a Boolean that says if possDiv is a valid divisor or not
def isDivisor(origNum,possDiv):
	if(origNum % possDiv == 0):
		possDiv = True
	else:
		possDiv = False
		
	numIsDiv = possDiv
	return numIsDiv
	
# sumDivisors() returns the sum of the divisors of a number
# Input:  num;      an integer that will have its divisors added up
# Output: sumDiv;  sum of all the divisors of a number
def sumDivisors(num):
	sumDiv = 0
	count = 1
	while(count < num + 1):
		if(count == num):
			return sumDiv
		elif(num % count == 0):
			sumDiv += count
		count+=1
		
	return sumDiv

# printTableLine() Prints the information for one number on one line
#                  of the table
# Input:  num,odd,prime,,perf,square,tri; num is an integer, and perf is a string
#							    odd,prime,square, and tri are Booleans   
# Output:             none(print function)
def printTableLine(num,odd,prime,perf,square,tri):
	print(num,"",end="")
	if(odd == True):
		print("\t",ODD,end="")
	if(odd == False):
		print("\t",EVEN,end="")
	if(prime == True):
		print("\t  ",PRI,end="")
	if(prime == False):
		print("\t",COM,end="")
	if(prime == NEI):
		print("\t  ",NEI,end="")
	if(perf == PERF):
		print("\t",PERF,end="")
	if(perf == ABD):
		print("\t",ABD,end="")
	if(perf == DEF):
		print("\t",DEF,end="")
	if(square == True):
		print("\t",SQU,end="")
	if(square == False):
		print("\t",end="")
	if(tri == True):
		print("\t",TRI,end="")
	if(tri == False):
		print("\t",end="")
	print("")
	
def main():
	printGreeting()
	print("Start with which positive integer?")
	firstNum = getValidInt(MIN_NUM,MAX_NUM)
	#Makes sure 2nd integer is greater than first
	print("End with which positive integer")
	secondNum = getValidInt(firstNum,MAX_NUM)

	printTableHead()
	
	count = firstNum

	while(count <= secondNum):
		#Functions are called for each number
		odd = isOdd(count)
		prime = isPrime(count)
		perfect = checkForPerfect(count)
		square = isSquare(count)
		triangle = isTriangular(count)
		printTableLine(count,odd,prime,perfect,square,triangle)
			
		count +=1
      
main()
