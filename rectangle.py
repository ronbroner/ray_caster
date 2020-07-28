import math
from point import *


# Written by Ron Broner 
# All rights reserved 

class Rectangle():

	# Initialize all variables needed to draw a rectangle
	def __init__(self, canvas,x,y,width,height):
		# Drawing surface canvas
		self.canvas = canvas

		# Coordinates of the top left corner of the rectangle 
		self.p = Point(x,y)

		# Width and height of the rectangle
		self.width = width 
		self.height = height

		# Initialize the color of the rectangle to be white
		self.color = 'white' 

		# Draw the rectangle object on the canvas
		self.shape = canvas.create_rectangle(self.p.getPointCoords()[0],self.p.getPointCoords()[1],self.p.getPointCoords()[0]+self.width,self.p.getPointCoords()[1]+self.width,fill=self.color,outline="")

	# Move the coordinates of the top left corner of the rectangle to (x,y)
	def move(self,x,y):
		self.p.setPoint(x,y)

	# Change the width and height of the rectangle
	def resize(self,width,height):
		self.width = width
		self.height = height

	# Draw the rectangle object on the canvas given the current coordinates, width/height, and color
	def draw(self):
		self.canvas.coords(self.shape,self.p.getPointCoords()[0],self.p.getPointCoords()[1],self.p.getPointCoords()[0]+self.width,self.p.getPointCoords()[1]+self.height)
		self.canvas.itemconfig(self.shape, fill=self.color)

	# Hide the rectangle by setting all dimensions to 0 
	def hide(self):
		self.canvas.coords(self.shape,0,0,0,0)

	# Change the color profile of the rectangle
	def changeColor(self,rgb):
		self.color = "#%02x%02x%02x" % (rgb)
		