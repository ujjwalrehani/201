# File: hw5_part1.py
# Author: Ujjwal Rehani
# Date: 3/31/17
# Section: 21
# E-mail: urehani1@umbc.edu
# Description:
# 	Calculates the distance between two points

# distance() calculates the distance between two points
# Input: point1; a tuple containing an X and a Y value
# 		 point2; a tuple containing an X and a Y value
# Output: ans; a float of the calculated distance
def distance(point1,point2):
	
	#Gets the coordinates from the tuple
	firstX = point1[0]
	secondX = point2[0]
	firstY = point1[1]
	secondY = point2[1]
	
	#Calculates the difference and their total sum
	xDist = (secondX - firstX)**2
	yDist = (secondY - firstY)**2
	sumDist = (xDist + yDist)
	
	#Calculates distance
	ans = float(sumDist**0.5)
	return ans

def main():
	print("This program will ask for two points, and")
	print("will compute the distance between the two")
	
	#Gets the first coordinate
	firstX = int(input("Please enter a value for x1: "))
	firstY = int(input("Please enter a value for y1: "))
	firstCoord = (firstX,firstY)
	
	#Gets the second coordinate
	secondX = int(input("Please enter a value for x2: "))
	secondY = int(input("Please enter a value for xy: "))
	secondCoord = (secondX,secondY)
	
	#Calls distance function
	totalDistance = distance(firstCoord,secondCoord)
	
	print("The distance betwen",firstCoord,"and",secondCoord,"is",totalDistance)

main()
	