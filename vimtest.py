from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Labeler")
root.geometry("200x400")

app = Frame(root)
app.grid()
button1 = Button(app, text ="This is a button")
label = Label(app, text = "This is a label!")
button2 = Button(app)

label.grid()
button1.grid()
button2.grid()
button2.configure(text = "this will show text")

button3 = Button(app)
button3.grid()
button3["text"] = "This will also show"
#kick off the event loop
root.mainloop()
