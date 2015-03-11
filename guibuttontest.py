
from Tkinter import *

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.count=0
		self.create_widgets()

	def addToCount(self):
		self.count = self.count+1
		self.countLabel['text'] = str(self.count)

	def subtractToCount(self):
		self.count = self.count -1
		self.countLabel['text'] = str(self.count)

	def create_widgets(self):
		self.button1 = Button(self, text = "Add to count")
		self.button1['command'] = self.addToCount
		self.button1.grid()

		self.button2= Button(self)
		self.button2["text"] = "Take Away from count"
		self.button2['command'] = self.subtractToCount
		self.button2.grid()
		
		self.countLabel = Label(self)
		self.countLabel.configure(text = str(self.count))
		self.countLabel.grid()

root = Tk()
root.title("ButtonLand")
root.geometry("300x300")

app= Application(root)

root.mainloop()
