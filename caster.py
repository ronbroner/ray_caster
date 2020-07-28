import math
from point import *
from line import *

# Written by Ron Broner 
# All rights reserved 

class Caster():

	# Initialize all variables local to 2D raycasting
	def __init__(self,canvas):
		#drawing surface canvas
		self.canvas = canvas
		# Coordinates of the mouse pointer
		self.mouseCoords = Point(0,0)

		# Potential New obstacle endpoints (x1,y1) -> (x2,y2)
		self.click = 0
		self.x1 = 0
		self.x2 = 0
		self.y1 = 0
		self.y2 = 0
		
		# Ray parameters
		self.rayWidth = 1
		self.numRays = 240
		self.rays = []

		# Angle Subtended by rays
		self.viewAngle = 60
		self.viewAngleRef = 0

		# Obstacle Parameters
		self.obstacleWidth = 3
		self.numObstacles = 0
		self.obstacles = []

		# Predefined obstacle "maps"
		self.obstacleMode = 1

		# Initialize the obstacles
		self.potentialObstacle = Line(self.canvas,0,0,0,0,self.obstacleWidth)
		self.potentialObstacleSignal = False

		# Initialize the rays
		for i in range(self.numRays):
			self.rays.append(Line(self.canvas,0,0,0,0,self.rayWidth))

	# Updates mouse location in frame (2D raycaster fram only)
	def updateMouse(self,x,y):
		self.mouseCoords.x = x
		self.mouseCoords.y = y

	# Creates a predefined array of obstacles (rather than user created)
	def preDefinedObstacles(self,mode):
		# mode 1 : Maze
		if mode == 1:
			l = 300
			x = 100
			y = 400
			counter = 0
			numRevs = 2
			while numRevs >= 0:
				if counter == 0:
					self.obstacles.append(Line(self.canvas,x,y,x,y-l,self.obstacleWidth))
					y = y-l
				elif counter == 1:
					self.obstacles.append(Line(self.canvas,x,y,x+l,y,self.obstacleWidth))
					x = x+l
				elif counter == 2:
					self.obstacles.append(Line(self.canvas,x,y,x,y+l,self.obstacleWidth))
					y = y+l
				elif counter == 3:
					self.obstacles.append(Line(self.canvas,x,y,x-l,y,self.obstacleWidth))
					x = x-l
					numRevs = numRevs - 1
				l = l-20
				counter = (counter + 1)%4
				self.numObstacles = self.numObstacles + 1

	# Calculates the geometry of rays (length, intersection, etc.) as if there are no obstacles
	# This makes further calcultions easier.
	def calculateUnblockedRays(self):
		for i in range(self.numRays):
			rayAngle = (i/float(self.numRays))*(2*math.pi)*(self.viewAngle/360.0)
			self.rays[i].move(self.mouseCoords.x,self.mouseCoords.y,self.mouseCoords.x+1000*math.cos(rayAngle+self.viewAngleRef),self.mouseCoords.y+1000*math.sin(rayAngle+self.viewAngleRef)) # 1000 is just a big number (outside of screen)
		

	# Uses both the list of rays and obstacles to calculate the geometry of the rays (length, intersection, etc.)
	# Method goes through all rays and for each one finds the nearest obstacle that intersects with it, and 
	# subsequently redraws the rays to this intersection points.
	def calculateBlockedRays(self):
		for i in range(self.numRays):
			# Initialize minimum intersection point (minX,minY) to some arbitrarily large number
			minX = float('inf')
			minY = float('inf') 
			minDist = float('inf')

			# Find where the full rays intersect with the obstacles and redraw the rays
			# based on that intersection point
			for j in range(self.numObstacles):
				intersectionPoint = Line.intersection(self.rays[i],self.obstacles[j])
				if intersectionPoint is not None:
					distX = intersectionPoint[0]-self.mouseCoords.x
					distY = intersectionPoint[1]-self.mouseCoords.y
					dist = math.sqrt(distX**2 + distY**2)

					if dist < minDist:
						minX = intersectionPoint[0]
						minY = intersectionPoint[1]
						minDist = dist
					self.rays[i].move(self.mouseCoords.x,self.mouseCoords.y,minX,minY) 
			self.rays[i].draw()
			
