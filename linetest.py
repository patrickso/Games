from Tkinter import *
import time
def slope(coords):
	return (coords[1]-coords[3])/(coords[0]-coords[2])
def findb(coords):
	return coords[1]-(slope(coords)*coords[0])
def online(line,ball):
	if (ball[1] == ball[0]*slope(line)+findb(line)) :
		return True
 	return False
print slope([1,1,2,2])
print findb([2,1,3,2])
print online([1.0,1.0,2.0,2.0],[1.5,1.5])
a = Canvas(100,100)
b = a.create_line(0,0,0,0)
print a.coords(b)
b.coords(1,1,1,1)
print a.coords(b)
