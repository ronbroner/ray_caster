# Written by Ron Broner 
# All rights reserved 

class Point():

	# Initilize Coordinates of point to (x,y)
	def __init__(self,x,y):
		self.x = x
		self.y = y

	# Return Coordinates of point as a tuple (x,y)
	def getPointCoords(self):
		return([self.x,self.y])

	# Change the coordinates of the point to (x,y)
	def setPoint(self,x,y):
		self.x = x
		self.y = y

	# Print the coordinate of the point to the console.
	def printPoint(self):
		print("("+str(self.x) + "," + str(self.y) + ")")