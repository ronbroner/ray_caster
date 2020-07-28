# Written by Ron Broner 
# All rights reserved 

class Circle():

	# Initialize all variables needed to draw a circle
	def __init__(self,canvas, x1,y1,r):
		# Drawing surface canvas
		self.canvas = canvas

		# Coordinates of center of circle (x1,y1)
		self.x1 = x1
		self.y1 = y1

		# Radius of the circle
		self.r = r

		# Draw the circle object on the canvas
		self.shape = canvas.create_oval(0,0,0,0,fill='black')

	# Returns the coordinates of the circle
	def getCoords(self):
		print("("+str(self.x1)+","+str(self.y1))

	# Changes coordinates of the circle
	def move(self,x1,y1,x2,y2):
		self.canvas.coords(self.shape,x1,y1,x2,y2)
