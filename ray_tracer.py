#!/usr/bin/env python3


# Written by Ron Broner 
# All rights reserved 

from tkinter import *
from random import *
import time
import math
import sys

from line import *
from circle import *
from rectangle import *

from caster import *
from render import *

windowWidth = 480
windowHeight = 500

# Define the First window - 2D Ray Caster View
master = Tk()
master.title('Ray Caster - 2D View')
master.geometry('%dx%d+%d+%d' % (windowHeight, windowWidth, 100, 100))
master.minsize(windowWidth,windowWidth) # Make window size fixed
master.maxsize(windowWidth,windowWidth)
canvas2d = Canvas(master,width=windowWidth, height=windowHeight,highlightthickness=0)
canvas2d.pack()


# Define the Second window - Ray Caster Rendering
slave = Tk()
slave.title('Ray Caster - Rendering')
slave.geometry('%dx%d+%d+%d' % (windowHeight, windowWidth, windowWidth + 200, 100))
slave.minsize(windowWidth,windowWidth) # Make window size fixed
slave.maxsize(windowWidth,windowWidth)
canvas3d = Canvas(slave,width=windowWidth, height=windowHeight, highlightthickness=0,background='white',bd=-2)
canvas3d.pack()



##### Set up 2D Raycaster Object ####
cast = Caster(canvas2d)

###### Set up 3D Rendering Object #######
rend = Render(canvas3d,windowWidth,windowHeight,cast.numRays)


# Click once to set up the first endpoint of a new obstacle, then as you move the mouse you will drag 
# around the second endpoint until you click again where you define the second endpoint of the obstacle.
def mouse_click(event):
	# First click
	if cast.click == 0:
		# Coordinates of the first endpoint of the line
		cast.x1 = event.x
		cast.y1 = event.y

		# Flag to indicate that you clicked once and are in the middle of placing a new obstacle
		cast.potentialObstacleSignal = True 
	# Second click
	elif cast.click == 1:
		# Coordinates of the second endpoint of the line
		cast.x2 = event.x
		cast.y2 = event.y

		# Draw the final new obstacle
		cast.obstacles.append(Line(canvas2d,cast.x1,cast.y1,cast.x2,cast.y2,cast.obstacleWidth)) 

		# increment the number of obstacle by 1
		cast.numObstacles = cast.numObstacles + 1 

		# Flag to indicate the new obstacle has been placed
		cast.potentialObstacleSignal = False 
	cast.click = (cast.click+1)%2

# Move the mouse location around the window to change the location of the "light source" or pov. Every time the
# mouse is moved all the rays are recalculated and subsequently the rendering is recalculated.
def mouse_move(event):
	# Update mouse coordinates
	cast.updateMouse(event.x,event.y)
	
	# Uses the flag from the mouse_click method to show the new potential obstacle line
	if cast.potentialObstacleSignal:
		cast.potentialObstacle.move(cast.x1,cast.y1,cast.mouseCoords.x,cast.mouseCoords.y)
	else:
		cast.potentialObstacle.move(0,0,0,0)
	cast.potentialObstacle.draw()

	# Calculate rays and rendering
	runCalculations()


# Method calls on all the "calculation" helper methods (i.e find/draw the location and length of all rays in the 
# raycaster window and then the rendered rays in the rendering window 
def runCalculations():
	# Changes to 2d below
	cast.calculateUnblockedRays()
	cast.calculateBlockedRays()

	# Changes to 3d below
	rend.updateRays(cast.rays)


# ******** Key Bindings **********

# Allows you to cancel drawing a new obstacle	
def escape(event):
	cast.potentialObstacleSignal = False
	cast.click = 0
	cast.potentialObstacle.move(0,0,0,0)
	cast.potentialObstacle.draw()

# Remove most recently drawn obstacle
def delete(event):
	if cast.numObstacles > 0:
		ob = cast.obstacles.pop()
		ob.move(0,0,0,0)
		ob.draw()
		cast.numObstacles = cast.numObstacles - 1
		runCalculations()

# End program if Enter is pressed
def enter(event):
	sys.exit(0)

# rotate 2D ray caster view angle and rendering counter-clockwise
def left(event):
	cast.viewAngleRef = cast.viewAngleRef - 0.1
	runCalculations()

# rotate 2D ray caster view angle and rendering clockwise
def right(event):
	cast.viewAngleRef = cast.viewAngleRef + 0.1
	runCalculations()

# Moves fowards in 2D ray caster and rendering by 5 unit lengths
def forward(event):
	cast.moveForwardBackwards(5)
	runCalculations()

# Moves backwards in 2D ray caster and rendering by 5 unit lengths
def backward(event):
	cast.moveForwardBackwards(-5)
	runCalculations()

# moves the pov up 5 pixels when the up arrow is pressed
def up(event):
	rend.moveUpDown(5)
	runCalculations()

# moves the pov down 5 pixels when the down arrow is pressed
def down(event):
	rend.moveUpDown(-5)
	runCalculations()





# setup keybindings for 2D  below
canvas2d.focus_set()
canvas2d.bind("<Button-1>", mouse_click)
canvas2d.bind("<Motion>",mouse_move)
canvas2d.bind("<Escape>", escape)
canvas2d.bind("<BackSpace>", delete)
canvas2d.bind("<Return>",enter)
canvas2d.bind('<Left>', left)
canvas2d.bind('<Right>', right)
canvas2d.bind('<Up>', forward)
canvas2d.bind('<Down>', backward)
cast.preDefinedObstacles(cast.obstacleMode)

# setup keybindings for 3D  below (bindings still mostly for 2d window)
canvas3d.focus_set()
canvas3d.bind("<Return>",enter)
canvas2d.bind("<w>",up)
canvas2d.bind("<s>",down)
 
runCalculations() # makes everything appear on launch rather than after first click

# Loop to refresh both windows
canvas3d.mainloop()
canvas2d.mainloop()
