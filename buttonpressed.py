from Tkinter import *
import time


class Node(int):
	def __init__(self):
		self.item = int
		self.right = None
	
	def getitem(self):
		return self.item
class Application(Frame):

	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.up = 0
		self.tempx = None
		self.tempy = None
		self.direct = []
		self.direct.append(0)
		self.pressed = 0
		self.score = 0
		self.highscore = 0
		self.re = 0
		self.create_widgets()

	def create_widgets(self):
		self.sheet = Canvas(self, width=300, height=500)
		self.ball = []
		self.ball.append(self.sheet.create_oval(150,30,160,40, fill="red", tags=1))
		self.tramp = self.sheet.create_line(1,2,3,4)
		self.play = self.sheet.create_text(150,125, text = 'Play', font=10)
		self.counter = self.sheet.create_text(250,50, text='Score: ' + str(self.score))
		self.hscore= self.sheet.create_text(240,30,text= 'Highscore: ' + str(self.highscore))
		self.rec = self.sheet.create_rectangle(100,100,200,150)
		self.border = self.sheet.create_rectangle(0,0,300,500)
		self.sheet.grid()
		

	def newline(self, event):
		if self.up == 0:
			self.tempx = event.x
			self.tempy = event.y
			self.up = 1
		else:
			self.sheet.coords(self.tramp,event.x,event.y,self.tempx,self.tempy)
			self.up = 0
	def mouseMoved(self, event):
		pass	
	def bounceup(self,ball):
		self.sheet.itemconfig(ball, tags= -1*float(self.sheet.itemcget(ball,'tags')))	
	
	def vel(self, ball):
		if self.pressed ==0:
			return 0
#			if self.sheet.coords(ball)[1] > 90:
#				self.bounceup(ball)
		if float(self.sheet.itemcget(ball, 'tags')) > 0:
			if 490 -  self.sheet.coords(ball)[1] < float(self.sheet.itemcget(ball, 'tags')):
				self.sheet.itemconfig(ball, tags= -1*float(self.sheet.itemcget(ball, 'tags')) )
				self.score = 0
				self.sheet.itemconfig(self.counter, text= 'Score: '+ str(self.score))
				self.re = 1
				if self.sheet.itemcget(ball,'fill') == 'red':
					self.sheet.itemconfig(ball, fill = 'blue')
				else:
					self.sheet.itemconfig(ball, fill = 'red')
				return 490 -  self.sheet.coords(ball)[1] 
		self.sheet.itemconfig(ball, tags = float(self.sheet.itemcget(ball, 'tags')) + .2)
		return self.sheet.itemcget(ball, 'tags')

	def trampcheck(self,ball):
		if (offline(self.sheet.coords(self.tramp),self.sheet.coords(ball))) or (self.sheet.coords(ball)[0] < findmin(self.sheet.coords(self.tramp)[0],self.sheet.coords(self.tramp)[2])-3 or self.sheet.coords(ball)[0] > findmax(self.sheet.coords(self.tramp)[0],self.sheet.coords(self.tramp)[2])+3):
			return False
		return True
	
	def angle(self,n):
		self.direct[n] =   5*slope(self.sheet.coords(self.tramp))
		return self.direct[n]

	def trampinteract(self,ball,n):
		b = self.trampcheck(ball)
		if not b:
			self.sheet.move(ball, self.direct[n], self.vel(ball))
		else:	
			self.sheet.itemconfig(ball, tags = -1*float(self.sheet.itemcget(ball, 'tags')))
			self.sheet.move(ball, self.angle(n),float(self.sheet.itemcget(ball, 'tags')))
			self.sheet.coords(self.tramp,-1,-2,-3,-4)
			self.score = self.score + 1
			self.sheet.itemconfig(self.counter, text='Score: ' + str(self.score))
			if self.score>self.highscore:
				self.highscore=self.score
				self.sheet.itemconfig(self.hscore, text='Highscore: ' + str(self.highscore))
			if self.score % 5 == 0:
				app.ball.append(self.sheet.create_oval(150,-30,160,-40, fill="red", tags=0))
				app.direct.append(0)
			

	def wallcheck(self,ball,n):
		if self.sheet.coords(ball)[0] < 5 or self.sheet.coords(ball)[0] > 290:
			self.direct[n] = -1*self.direct[n]

	def pressplay(self,event):
		if event.x > 100 and event.x < 200 and event.y > 100 and event.y < 150:
			self.sheet.delete(self.play)
			self.sheet.delete(self.rec)
			self.sheet.itemconfig(self.counter,fill='black')
			self.sheet.itemconfig(self.hscore,fill='black')
			self.sheet.itemconfig(self.ball[0], fill='red')
			self.pressed = 1
	
	def restart(self):
		if self.re ==1:
			for x in range(len(self.ball)):
				self.sheet.delete(self.ball[len(self.ball)-1-x])
			for x in range(len(self.ball)):
				self.ball.pop()
			self.direct = [0]
			self.ball.append(self.sheet.create_oval(150,30,160,40,fill='red', tags = 1))
			self.play = self.sheet.create_text(150,125, text = 'Play', font=10)
			self.sheet.coords(self.tramp,-1,-2,-3,-4)
			self.rec = self.sheet.create_rectangle(100,100,200,150)
			self.re = 0
			self.pressed =0

		
def callback(event):
	if app.pressed == 0:
		app.pressplay(event)
	else:
		app.newline(event)

def motion(event):
	app.mouseMoved(event)
def slope(coords):
	return (coords[1]-coords[3])/(coords[0]-coords[2])
def findb(coords):
	return coords[1]-(slope(coords)*coords[0])
def offline(line,ball):
	if (ball[1] < ball[0]*slope(line)+findb(line)-15) or  (ball[1] > ball[0]*slope(line)+findb(line)+3)  :
		return True
 	return False
		

def findmin(x,y):
	if x<y:
		return x
	else:
		return y
def findmax(x,y):
	if x>y:
		return x
	return y
root=Tk()
root.geometry('300x500')
root.title('Hello World')
app = Application(root)

while True:
	time.sleep(0.025)
	root.bind('<Button-1>', callback)
	root.bind('<Motion>', motion)
	i =0
	for x in app.ball:
		app.wallcheck(x,i)
		app.trampinteract(x,i)
		i = i+1
	app.restart()
	app.sheet.update()


root.mainloop()

