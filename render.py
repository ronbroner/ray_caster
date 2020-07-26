from rectangle import *

class Render():

	def __init__(self,canvas,winWidth,winHeight,rayCount):
		self.canvas = canvas
		self.winHeight = winHeight
		self.winWidth = winWidth
		self.rayCount = rayCount
		self.rectWidth = winWidth/rayCount
		self.renderRects = []
		for i in range(rayCount):
			self.renderRects.append(Rectangle(canvas,0,0,0,0))




	def updateRays(self,rays):
		for i in range(len(self.renderRects)):
			dist = rays[i].getLength()

			# Change rectangle size
			if dist == 0:
				height = self.winHeight
			else:
				height = 10000/dist
			self.renderRects[i].move(i*self.winWidth/self.rayCount,self.winHeight/2-height/2) # FIX ME
			self.renderRects[i].resize(self.rectWidth,height) #FIX ME

			# Change rectangle color
			fFactor = 2
			c = dist/fFactor
			if c > 255:
				c = 255
			self.renderRects[i].changeColor((c,c,c)) # FIX ME

			# Finally draw the fixed rectangles 
			self.renderRects[i].draw()

