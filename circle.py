
class Circle():


	def __init__(self,canvas, x1,y1,r):
		self.canvas = canvas
		self.x1 = x1
		self.y1 = y1
		self.r = r
		self.shape = canvas.create_oval(0,0,0,0,fill='black')


	def getCoords(self):
		print("("+str(self.x1)+","+str(self.y1))


	def move(self,x1,y1,x2,y2):
		self.canvas.coords(self.shape,x1,y1,x2,y2)
