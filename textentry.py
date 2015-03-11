from Tkinter import *

class Application(Frame):

	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
	
	def create_widgets(self):
		self.instructions = Label(self, text = "Whats the password Nigga")
		self.instructions.grid(row=0,column=0,columnspan=2,sticky = W)
		self.password = Entry(self)
		self.password.grid(row=1,column=1,sticky=W)
		

		self.submitbut = Button(self, text= "Submit", command= self.test)
		self.submitbut.grid(row=2,column=0,sticky=W)
		self.text = Text(self, width=35, height=5, wrap = WORD)
		self.text.grid(row = 3, column=0,columnspan=2,sticky=W)

	def test(self):
		content=self.password.get()
		if content == "password":
			message = "You win"
		else:
			message = "Access Denied"
		self.text.delete(0.0,END)
		self.text.insert(0.0,message)
root= Tk()
root.title("Nigga Shit")
root.geometry("300x300")
app = Application(root)

root.mainloop()
