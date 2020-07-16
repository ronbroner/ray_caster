
class Line():



	def __init__(self, canvas,x1,y1,x2,y2):
		self.canvas = canvas
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.shape = canvas.create_line(x1,y1,x2,y2)



	def getCoords(self):
		print("("+str(self.x1)+","+str(self.y1)+") -> "+"("+str(self.x2)+","+str(self.y2)+")")

	def move(self,x1,y1,x2,y2):
		self.canvas.coords(self.shape,x1,y1,x2,y2)

	@staticmethod
	def intersection(l1,l2):
		return
