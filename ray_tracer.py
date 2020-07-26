#!/usr/bin/python
from Tkinter import *
from random import *
import time
import math
import sys

from line import *
from circle import *
from rectangle import *

from render import *

windowWidth = 480
windowHeight = 500

master = Tk()
master.title('Ray Tracer - 2D View')
master.geometry('%dx%d+%d+%d' % (windowHeight, windowWidth, 100, 100))
canvas2d = Canvas(master,width=windowWidth, height=windowHeight,highlightthickness=0)
canvas2d.pack()



slave = Tk()
slave.title('Ray Tracer - Rendering')
slave.geometry('%dx%d+%d+%d' % (windowHeight, windowWidth, windowWidth + 200, 100))
canvas3d = Canvas(slave,width=windowWidth, height=windowHeight, highlightthickness=0,background='white',bd=-2)
canvas3d.pack()


###### 2D VARIABLES #######
 
mouseX = 0
mouseY = 0

click = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0


rayWidth = 1
numRays = 240
rays = []


viewAngle = 60
viewAngleRef = 0


obstacleWidth = 3
numObstacles = 0
obstacles = []

obstacleMode = 1

potentialObstacle = Line(canvas2d,0,0,0,0,obstacleWidth)
potentialObstacleSignal = False


for i in range(numRays):
	rays.append(Line(canvas2d,0,0,0,0,rayWidth))



###### 3D VARIABLES #######
rend = Render(canvas3d,windowWidth,windowHeight,numRays)
#canvas2d.create_rectangle(0,0,100,100,fill="#%02x%02x%02x" % (150,150,150) ,outline="")
#canvas2d.create_rectangle(100,100,200,200,fill="#%02x%02x%02x" % (190,190,190) ,outline="")

# mode 0 = none
# mode 1 = simple maze

def preDefinedObstacles(mode):
	global numObstacles
	if mode == 1:
		l = 300
		x = 100
		y = 400
		counter = 0
		numRevs = 2
		while numRevs >= 0:
			if counter == 0:
				obstacles.append(Line(canvas2d,x,y,x,y-l,obstacleWidth))
				y = y-l
			elif counter == 1:
				obstacles.append(Line(canvas2d,x,y,x+l,y,obstacleWidth))
				x = x+l
			elif counter == 2:
				obstacles.append(Line(canvas2d,x,y,x,y+l,obstacleWidth))
				y = y+l
			elif counter == 3:
				obstacles.append(Line(canvas2d,x,y,x-l,y,obstacleWidth))
				x = x-l
				numRevs = numRevs - 1
			l = l-20
			counter = (counter + 1)%4
			numObstacles = numObstacles + 1


def calculateUnblockedRays():
	for i in range(numRays):
		rayAngle = (i/float(numRays))*(2*math.pi)*(viewAngle/360.0)
		rays[i].move(mouseX,mouseY,mouseX+1000*math.cos(rayAngle+viewAngleRef),mouseY+1000*math.sin(rayAngle+viewAngleRef)) # 1000 is just a big number (outside of screen)
	


def calculateBlockedRays():
	for i in range(numRays):

		rayAngle = (i/float(numRays))*(2*math.pi)*(viewAngle/360.0)
		minX = float('inf') # some large number
		minY = float('inf')
		minDist = float('inf')

		
		for j in range(numObstacles):
			intersectionPoint = Line.intersection(rays[i],obstacles[j])
			if intersectionPoint is not None:
				distX = intersectionPoint[0]-mouseX
				distY = intersectionPoint[1]-mouseY
				dist = math.sqrt(distX**2 + distY**2)

				if dist < minDist:
					minX = intersectionPoint[0]
					minY = intersectionPoint[1]
					minDist = dist
				rays[i].move(mouseX,mouseY,minX,minY) 
		rays[i].draw()
		



def mouse_click(event):
	global click,x1,x2,y1,y2,numObstacles,potentialObstacleSignal
	if click == 0:
		x1 = event.x
		y1 = event.y
		potentialObstacleSignal = True
	elif click == 1:
		x2 = event.x
		y2 = event.y
		obstacles.append(Line(canvas2d,x1,y1,x2,y2,obstacleWidth))
		numObstacles = numObstacles + 1
		potentialObstacleSignal = False
	click = (click+1)%2

def mouse_move(event):
	global x1,y1,potentialObstacle,potentialObstacleSignal,mouseX,mouseY

	mouseX = event.x
	mouseY = event.y
	
	if potentialObstacleSignal:
		potentialObstacle.move(x1,y1,mouseX,mouseY)
	else:
		potentialObstacle.move(0,0,0,0)
	potentialObstacle.draw()

	# Changes to 2d below
	calculateUnblockedRays()
	calculateBlockedRays()

	# Changes to 3d below
	rend.updateRays(rays)


# ******** Key Bindings **********

# Allows you to cancel drawing a new obstacle	
def escape(event):
	global potentialObstacle, potentialObstacleSignal, click
	potentialObstacleSignal = False
	click = 0
	potentialObstacle.move(0,0,0,0)
	potentialObstacle.draw()

# Remove most recently drawn obstacle
def delete(event):
	global numObstacles
	if numObstacles > 0:
		ob = obstacles.pop()
		ob.move(0,0,0,0)
		ob.draw()
		numObstacles = numObstacles - 1
		calculateUnblockedRays()
		calculateBlockedRays()

def enter(event):
	sys.exit(0)

def aKey(event):
	global viewAngleRef
	viewAngleRef = viewAngleRef - 0.1
	# Changes to 2d below
	calculateUnblockedRays()
	calculateBlockedRays()

	# Changes to 3d below
	rend.updateRays(rays)



def dKey(event):
	global viewAngleRef
	viewAngleRef = viewAngleRef + 0.1
	# Changes to 2d below
	calculateUnblockedRays()
	calculateBlockedRays()

	# Changes to 3d below
	rend.updateRays(rays)


# setip for 2D  below
canvas2d.focus_set()
canvas2d.bind("<Button-1>", mouse_click)
canvas2d.bind("<Motion>",mouse_move)
canvas2d.bind("<Escape>", escape)
canvas2d.bind("<BackSpace>", delete)
canvas2d.bind("<Return>",enter)
canvas2d.bind('<a>', aKey)
canvas2d.bind('<d>', dKey)
preDefinedObstacles(obstacleMode)

# setup for 3D  below
canvas3d.focus_set()
canvas3d.bind("<Return>",enter)




canvas3d.mainloop()
canvas2d.mainloop()
