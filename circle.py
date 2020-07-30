from point import *

# Written by Ron Broner 
# All rights reserved 

class Circle():

	# Initialize all variables needed to draw a circle
	def __init__(self,canvas, x,y,r,color='black'):
		# Drawing surface canvas
		self.canvas = canvas

		# Coordinates of center of circle (x,1)
		self.p = Point(x,y) 

		# Radius of the circle
		self.r = r

		# Draw the circle object on the canvas
		self.shape = canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)

	# Returns the coordinates of the circle
	def getCoords(self):
		print("("+str(self.p.getPointCoords()[0])+","+str(self.p.getPointCoords()[1]))

	# Changes center of circle to (x,y)
	def move(self,x,y):
		self.p.setPoint(x,y)

	# Change the radius of the circle
	def changeSize(self,r):
		self.r = r

	# Draws the circle using the existing center point coordinates and radius
	def draw(self):
		x = self.p.getPointCoords()[0]
		y = self.p.getPointCoords()[1]
		r = self.r
		self.canvas.coords(self.shape,x-r,y-r,x+r,y+r)
