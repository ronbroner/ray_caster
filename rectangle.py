import math
from point import *

class Rectangle():

	def __init__(self, canvas,x,y,width,height):
		self.canvas = canvas
		self.p = Point(x,y)
		self.width = width # Default line width =1
		self.height = height
		self.color = 'white' # Default color 
		self.shape = canvas.create_rectangle(self.p.getPointCoords()[0],self.p.getPointCoords()[1],self.p.getPointCoords()[0]+self.width,self.p.getPointCoords()[1]+self.width,fill=self.color,outline="")


	def move(self,x,y):
		self.p.setPoint(x,y)

	def resize(self,width,height):
		self.width = width
		self.height = height

	def draw(self):
		self.canvas.coords(self.shape,self.p.getPointCoords()[0],self.p.getPointCoords()[1],self.p.getPointCoords()[0]+self.width,self.p.getPointCoords()[1]+self.height)
		self.canvas.itemconfig(self.shape, fill=self.color)


	def hide(self):
		self.canvas.coords(self.shape,0,0,0,0)


	def changeColor(self,rgb):
		self.color = "#%02x%02x%02x" % (rgb)
		