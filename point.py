

class Point():


	def __init__(self,x,y):
		self.x = x
		self.y = y


	def getPointCoords(self):
		return([self.x,self.y])

	def setPoint(self,x,y):
		self.x = x
		self.y = y

	def printPoint(self):
		print("("+str(self.x) + "," + str(self.y) + ")")