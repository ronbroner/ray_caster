from rectangle import *

# Written by Ron Broner 
# All rights reserved 

class Render():

	# Initialize all variables local to 3D rendering
	def __init__(self,canvas,winWidth,winHeight,rayCount,viewAngle):
		# Drawing surface canvas
		self.canvas = canvas

		# Window dimensions
		self.winHeight = winHeight
		self.winWidth = winWidth

		# Number of rays
		self.rayCount = rayCount

		# Angle Subtended by rays
		self.viewAngle = viewAngle

		# Width of each rendered rectangle 
		self.rectWidth = winWidth/rayCount

		# Litst of rendered rectangles
		self.renderRects = []

		# Scaler constant to add to y coordinate to simulate moving up/down
		self.povHeight = 0

		# Initialize the rendered rectangles
		for i in range(rayCount):
			self.renderRects.append(Rectangle(canvas,0,0,0,0))

		# Initialize suplementary floor/sky rendered rectangles
		self.floorRects = []
		self.skyRects = []
		for i in range(rayCount):
			self.floorRects.append(Rectangle(canvas,0,0,0,0))
			self.skyRects.append(Rectangle(canvas,0,0,0,0))
			self.floorRects[i].changeColor((0,98,0))
			self.skyRects[i].changeColor((135,206,235))


	# Input: array of 2D rays (which come from the 2D Caster object)
	#
	# Goes through all the 2D rays and based on their length (i.e. function of intersection with obstacle)
	# draws an array of thin vertical rectangles (one per ray) which vary in size and shade to create the illusion of 
	# 3D depth perception. This method also draws the floor and sky, by basically drawing similar thin rectangles below 
	# and above the wall rectangles in green adnd blue respectively.

	def updateRays(self,rays):
		for i in range(len(self.renderRects)):

			# The following 2 lines correct the close up rounding effect by finding the angle of each ray from 
			# the cener ray and multipling the length of said ray by the cosine of the angle.
			# This helps make flat objects look flat up close instead of round
			angle = abs(i*(self.viewAngle/self.rayCount) - self.viewAngle/2) # calculate angle from center ray
			angle = angle*math.pi/180 # convert to radians

			# calculate the length of each ray (scaled by cosine of the angle)
			dist = rays[i].getLength()*math.cos(angle)

			# Change rectangle size
			if dist == 0:
				height = self.winHeight
			elif dist >=800:
				height = 0
			else:
				height = 10000/dist
			xCoord = i*self.winWidth/self.rayCount
			yCoord = self.winHeight/2-height/2 + self.povHeight

			self.renderRects[i].move(xCoord,yCoord) 
			self.renderRects[i].resize(self.rectWidth,height) 

			# Change rectangle color
			fFactor = 3
			c = int(dist/fFactor)
			if c > 255:
				c = 255
			self.renderRects[i].changeColor((c,c,c))

			# Finally draw the fixed rectangles 
			self.renderRects[i].draw()


			# Now draw the floor/sky

			self.floorRects[i].move(xCoord,yCoord+height) 
			self.floorRects[i].resize(self.rectWidth,self.winHeight-(yCoord+height)) 
			self.floorRects[i].draw()

			self.skyRects[i].move(xCoord,0) 
			self.skyRects[i].resize(self.rectWidth,yCoord) 
			self.skyRects[i].draw()

	# Moves the "Camera" POV to simulate tilting your head up/down
	def moveUpDown(self,amount):
		self.povHeight = self.povHeight + amount

	# Returns the POV height (the angle of polar head tilt)
	def getPovHeight(self):
		return self.povHeight
