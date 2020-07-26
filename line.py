from point import *
import math

class Line():


	def __init__(self, canvas,x1,y1,x2,y2,width):
		self.canvas = canvas
		self.p1 = Point(x1,y1)
		self.p2 = Point(x2,y2)
		self.width = width # Default line width =1
		self.shape = canvas.create_line(x1,y1,x2,y2,width=width)



	def printLine(self):
		print("(" + str(self.p1.getPointCoords()[0])+ ","+ str(self.p1.getPointCoords()[1]) + ") -> " + "(" + str(self.p2.getPointCoords()[0])+ ","+ str(self.p2.getPointCoords()[1]) + ")")
 
	def getFirst(self):
		return self.p1

	def getSecond(self):
		return self.p2

	def getLength(self):
		return math.sqrt((self.p1.getPointCoords()[0] - self.p2.getPointCoords()[0])**2 + (self.p1.getPointCoords()[1] - self.p2.getPointCoords()[1])**2)


	def move(self,x1,y1,x2,y2):
		self.p1.setPoint(x1,y1)
		self.p2.setPoint(x2,y2)

	def draw(self):
		x1 = self.p1.getPointCoords()[0]
		y1 = self.p1.getPointCoords()[1]
		x2 = self.p2.getPointCoords()[0]
		y2 = self.p2.getPointCoords()[1]
		self.canvas.coords(self.shape,x1,y1,x2,y2)

	def hide(self):
		self.canvas.coords(self.shape,0,0,0,0)

	# Inputs - (Line l1, Line l2):
	# l1 is ray (xa,ya) -> (xb,yb)
	# l2 is obstacle (xc,yc) -> (xd,yd)
	#
	# Output - list [x,y] where (x,y) are intersection point of l1 and l2:
	# 
	@staticmethod
	def intersection(l1,l2):
		A = l1.getFirst()
		B = l1.getSecond()
		C = l2.getFirst()
		D = l2.getSecond()

		xa = A.getPointCoords()[0]
		ya = A.getPointCoords()[1]
		xb = B.getPointCoords()[0]
		yb = B.getPointCoords()[1]
		xc = C.getPointCoords()[0]
		yc = C.getPointCoords()[1]
		xd = D.getPointCoords()[0]
		yd = D.getPointCoords()[1]




		x = 0
		y = 0



		# Note: must check with < because xa and xc are int, xb and xd are float
		# See Important Note below for more details

		if abs(xa-xb)<0.00001: 
			if xc == xd:
				return None
			else:
				m2 = float(yd-yc)/(xd-xc)
				b2 = yd - m2*xd
				x = xa
				y = m2*x+b2
		elif abs(xc-xd)<0.00001:
			m1 = float(yb-ya)/(xb-xa)
			b1 = ya - m1*xa
			x = xc
			y = m1*x+b1
		else:
			m1 = float(yb-ya)/(xb-xa)
			m2 = float(yd-yc)/(xd-xc)
			if (m1 == m2): # Parallel lines -- no intersection
				return None
			b1 = yb - m1*xb
			b2 = yd - m2*xd
			x = (b2-b1)/(m1-m2)
			y = m1*x+b1


		#  ******* IMPORTANT NOTE *******
		#  Need to round in order to avoid the following round off error
		# 		2 <= 2.0	    			True
		#		2 <= 2.0000000001			False
		# 
		#	The tailing 1 on the second example is an artifact of floating point arithmatic
		#	Rounding to 4 digits give us decent precision and removes this round of error
		#

		xa = round(xa,6)
		xb = round(xb,6)
		xc = round(xc,6)
		xd = round(xd,6)
		x = round(x,6)
		y = round(y,6)
	
		if (((x>=xd and x<=xc) or (x>=xc and x<=xd)) and ((y>=yd and y<=yc) or (y>=yc and y<=yd))) and (((x>=xb and x<=xa) or (x>=xa and x<=xb)) and ((y>=yb and y<=ya) or (y>=ya and y<=yb))):	
			"""
			print(" **** IN ******")
			print("Ray end points: (" + str(xa)+","+str(ya) + ") -> (" + str(xb)+","+str(yb) + ")")
			print("Obstacle end points: (" + str(xc)+","+str(yc) + ") -> (" + str(xd)+","+str(yd)+ ")")
			print("Intersection Point: " + str(x) + ","+str(y))
			dx = x-xa
			dy = y-ya
			dist = math.sqrt(dx**2 + dy**2)
			print("Distance: " + str(dist))
			print("***** IN (end) *******")
			"""
			return [x,y]
		else:
			"""
			print(" **** NONE *******")
			print("Ray end points: (" + str(xa)+","+str(ya) + ") -> (" + str(xb)+","+str(yb) + ")")
			print("Obstacle end points: (" + str(xc)+","+str(yc) + ") -> (" + str(xd)+","+str(yd)+ ")")
			print("Intersection (NONE) Point: " + str(x) + ","+str(y))
			print(" **** NONE (end) *****")
			"""
			return None
			



