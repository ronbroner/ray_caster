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
canvas = Canvas(master, width=windowHeight, height=windowWidth,highlightthickness=0)
canvas.pack()


click = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0


rayWidth = 1
numRays = 40
rays = []


obstacleWidth = 3
numObstacles = 0
obstacles = []



potentialObstacle = Line(canvas,0,0,0,0,obstacleWidth)
potentialObstacleSignal = False




for i in range(numRays):
	rays.append(Line(canvas,0,0,0,0,rayWidth))





def resetRays(x,y):
	
	for i in range(numRays):
		angle = (i/float(numRays))*(2*math.pi)
		rays[i].move(x,y,x+1000*math.cos(angle),y+1000*math.sin(angle)) # 1000 is just a big number (outside of screen)
	

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
	global x1,y1,potentialObstacle,potentialObstacleSignal

	x = event.x
	y = event.y
	
	if potentialObstacleSignal:
		potentialObstacle.move(x1,y1,x,y)
	else:
		potentialObstacle.move(0,0,0,0)
	potentialObstacle.draw()

	resetRays(x,y)

	for i in range(numRays):
		#rays[i].draw()
	
		angle = (i/float(numRays))*(2*math.pi)
		minX = float('inf') # some large number
		minY = float('inf')

		for j in range(numObstacles):
			intersectionPoint = Line.intersection(rays[i],obstacles[j])
			if intersectionPoint is not None:
				distX = intersectionPoint[0]-x
				distY = intersectionPoint[1]-y
				if abs(distX)<abs(minX) and abs(distY)<abs(minY):
					minX = intersectionPoint[0]
					minY = intersectionPoint[1]
				rays[i].move(x,y,minX,minY) 
		rays[i].draw()
	

# Allows you to cancel drawing a new obstacle	
def escape(event):
	global potentialObstacle, potentialObstacleSignal, click
	potentialObstacleSignal = False
	click = 0
	potentialObstacle.move(0,0,0,0)
	potentialObstacle.draw()



canvas.focus_set()
canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Motion>",mouse_move)
canvas.bind("<Escape>", escape)




canvas.mainloop()