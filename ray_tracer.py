#!/usr/bin/python
from Tkinter import *
from random import *
import time
import math


from line import *
from circle import*



windowWidth = 480
windowHeight = 500

master = Tk()
master.title('Ray Tracer - 2D View')
master.geometry('%dx%d+%d+%d' % (windowHeight, windowWidth, 100, 100))
canvas = Canvas(master,width=windowWidth, height=windowHeight,highlightthickness=0)
canvas.pack()



slave = Tk()
slave.title('Ray Tracer - Rendering')
slave.geometry('%dx%d+%d+%d' % (windowHeight, windowWidth, windowWidth + 200, 100))
canvas2 = Canvas(slave,width=windowWidth, height=windowHeight, highlightthickness=0)
canvas2.pack()


mouseX = 0
mouseY = 0

click = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0


rayWidth = 1
numRays = 40
rays = []


viewAngle = 60
viewAngleRef = 0


obstacleWidth = 3
numObstacles = 0
obstacles = []



potentialObstacle = Line(canvas,0,0,0,0,obstacleWidth)
potentialObstacleSignal = False




for i in range(numRays):
	rays.append(Line(canvas,0,0,0,0,rayWidth))





def calculateUnblockedRays():
	for i in range(numRays):
		rayAngle = (i/float(numRays))*(2*math.pi)*(viewAngle/360.0)
		rays[i].move(mouseX,mouseY,mouseX+1000*math.cos(rayAngle+viewAngleRef),mouseY+1000*math.sin(rayAngle+viewAngleRef)) # 1000 is just a big number (outside of screen)
	


def calculateBlockedRays():
	for i in range(numRays):
		#rays[i].draw()
		rayAngle = (i/float(numRays))*(2*math.pi)
		minX = float('inf') # some large number
		minY = float('inf')

		for j in range(numObstacles):
			intersectionPoint = Line.intersection(rays[i],obstacles[j])
			if intersectionPoint is not None:
				distX = intersectionPoint[0]-mouseX
				distY = intersectionPoint[1]-mouseY
				if abs(distX)<abs(minX) and abs(distY)<abs(minY):
					minX = intersectionPoint[0]
					minY = intersectionPoint[1]
				rays[i].move(mouseX,mouseY,minX,minY) 
		rays[i].draw()
		#print((viewAngle/360.0)*numRays)
		""""
		if i <= ((viewAngleRef + viewAngle)/360.0)*numRays and i >= (viewAngleRef/360.0)*numRays:
			rays[i].draw()
		else:
			print('hide')
			rays[i].hide()
		"""



def mouse_click(event):
	global click,x1,x2,y1,y2,numObstacles,potentialObstacleSignal
	if click == 0:
		x1 = event.x
		y1 = event.y
		potentialObstacleSignal = True
	elif click == 1:
		x2 = event.x
		y2 = event.y
		obstacles.append(Line(canvas,x1,y1,x2,y2,obstacleWidth))
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

	calculateUnblockedRays()
	calculateBlockedRays()


# Allows you to cancel drawing a new obstacle	
def escape(event):
	global potentialObstacle, potentialObstacleSignal, click
	potentialObstacleSignal = False
	click = 0
	potentialObstacle.move(0,0,0,0)
	potentialObstacle.draw()


def aKey(event):
	global viewAngleRef
	viewAngleRef = viewAngleRef - 0.1
	calculateUnblockedRays()
	calculateBlockedRays()



def dKey(event):
	global viewAngleRef
	viewAngleRef = viewAngleRef + 0.1
	calculateUnblockedRays()
	calculateBlockedRays()


canvas.focus_set()
canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Motion>",mouse_move)
canvas.bind("<Escape>", escape)
canvas.bind('<a>', aKey)
canvas.bind('<d>', dKey)



canvas.mainloop()