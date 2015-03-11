from Tkinter import *
import time

class Application(Frame):

	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()	

	def create_widgets(self):
		self.sheet = Canvas(height=750, width=1450)
		x = self.sheet
		x.pack()
		x.create_line(0,0,1450,750)
		x.create_line(0,750,1450,0)
		x.ball = x.create_oval(400,400,410,410,tags='hello', fill="red", activefill="blue")
		x.grid()
	def pressdown(event):
		print "clicked at"
root = Tk()
root.geometry("2000x1000")
root.title("hey there")
app = Application(root)
root.bind("<Button-1>", app.pressdown())
while True:
	time.sleep(.025)
	root.bind("<Button-1>", app.pressdown())
	if app.sheet.coords(app.sheet.ball)[0] > 1000:
		while app.sheet.coords(app.sheet.ball)[0] > 100:
			time.sleep(.025)
			app.sheet.move(app.sheet.ball, -3,0)
			app.sheet.update()
	app.sheet.move(app.sheet.ball, 3,0)
	app.sheet.update()
root.mainloop()
