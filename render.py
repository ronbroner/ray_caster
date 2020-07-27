from rectangle import *

class Render():

	def __init__(self,canvas,winWidth,winHeight,rayCount):
		self.canvas = canvas
		self.winHeight = winHeight
		self.winWidth = winWidth
		self.rayCount = rayCount
		self.rectWidth = winWidth/rayCount
		self.renderRects = []
		self.povHeight = 0
		for i in range(rayCount):
			self.renderRects.append(Rectangle(canvas,0,0,0,0))

		self.floorRects = []
		self.skyRects = []
		for i in range(rayCount):
			self.floorRects.append(Rectangle(canvas,0,0,0,0))
			self.skyRects.append(Rectangle(canvas,0,0,0,0))
			self.floorRects[i].changeColor((0,98,0))
			self.skyRects[i].changeColor((135,206,235))


	def updateRays(self,rays):
		for i in range(len(self.renderRects)):
			dist = rays[i].getLength()

			# Change rectangle size
			if dist == 0:
				height = self.winHeight
			elif dist >=900:
				height = 0
			else:
				height = 10000/dist
			xCoord = i*self.winWidth/self.rayCount
			yCoord = self.winHeight/2-height/2 + self.povHeight

			self.renderRects[i].move(xCoord,yCoord) 
			self.renderRects[i].resize(self.rectWidth,height) 

			# Change rectangle color
			fFactor = 3
			c = dist/fFactor
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

	def moveUpDown(self,amount):
		self.povHeight = self.povHeight + amount

	def getPovHeight(self):
		return self.povHeight




