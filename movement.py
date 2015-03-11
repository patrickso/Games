from Tkinter import *
import time

class Application(Frame):

	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		self.dot = Canvas(width=200,height=100)
		self.dot.pack()
		self.dot.create_line(0,0,200,100)
		self.dot.create_line(0,100,200,0,fill="red",dash=(4,4))
		self.dot.create_rectangle(50,25,150,75,fill="blue")
		self.up = Button(self, text="Up", command = self.rowUp)
		self.down = Button(self,text="Down", command = self.rowDown)
		self.left = Button(self, text="Left", command = self.colDown)
		self.right = Button(self, text="Right",command = self.colUp)
		self.dot.grid()
		self.up.grid(row=0, column=5, sticky = W)
		self.down.grid(row=5, column=5, sticky = W)
		self.left.grid(row=5, column=0, sticky = W)
		self.right.grid(row=5, column=10, sticky = W)
	def rowUp(self):
		pass
	def rowDown(self):
		pass
	def colUp(self):
		pass
	def colDown(self):
		pass
root = Tk()
root.title("Suppo")
root.geometry("1000x1000")
app = Application(root)

root.mainloop()
