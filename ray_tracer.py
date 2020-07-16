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
canvas = Canvas(master, width=windowHeight, height=windowWidth)
canvas.pack()


click = 0
x1 = 0
x2 = 0
y1 = 0
y2 = 0


numRays = 40
rays = []

numObstacles = 0
obstacles = []


for i in range(numRays):
	rays.append(Line(canvas,0,0,0,0))




source = Circle(canvas,0,0,5)


def mouse_click(event):
	global click,x1,x2,y1,y2,numObstacles
	if click == 0:
		x1 = event.x
		y1 = event.y
	elif click == 1:
		x2 = event.x
		y2 = event.y
		obstacles.append(Line(canvas,x1,y1,x2,y2))
		numObstacles = numObstacles + 1
	click = (click+1)%2

def mouse_move(event):
	global numObstacles
	x = event.x
	y = event.y
	for i in range(numRays):
		angle = (i/float(numRays))*(2*math.pi)
		minX = windowHeight # some large number
		for j in range(numObstacles):
			rays[i].move(x,y,1000*math.cos(angle),1000*math.sin(angle)) # 1000 is just a big number (outside of screen)




canvas.bind("<Button-1>", mouse_click)
canvas.bind("<Motion>",mouse_move)



canvas.mainloop()