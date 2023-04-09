#Shashwini Krishnan 
#Python side project
#Digital Clock -displays digital clock with date, time, and a random quote

#importing tkinter -Python GUI interface 
from tkinter import *
from tkinter.ttk import *

from time import strftime #converts the time to string

import requests #module to import random quotes
from threading import Thread

api="http://api.quotable.io/random" #site to get random quotes 

#creating tkinter window
root=Tk()
root.title("Shashi's Clock") #root refers to the root window of tkinter
root.geometry("350x180")
root.configure(background="black")
root.resizable(width=1440, height=900)
#creating function to display time on the label in the root window

def time(): #function to display time and date
	Time=strftime('%I:%M:%S %p') #%p shows AM/PM and %I makes the clock to be in 12H format
	weekday=strftime("%A")
	day=strftime("%d")
	month=strftime("%b")
	year=strftime("%Y")


	lbl.config(text=Time)
	lbl.after(1000,time) #1000 refers to 1000ms=1sec. This would lead the time 
	#display to change after 1sec. 
	lbl2.config(text=weekday +" "+ str(month) + " " + str(day) +"," + year)

def quote(): #function to generate random quotes
	global quotes

	for x in range(1): #generate only one quote
		random_quote=requests.get(api).json()
		quote=random_quote["content"]

#Function ends here

	lbl3.config(text=quote)

#styling the labels

lbl=Label(root, font=('Helvetica',45,'bold'), background='black', foreground='white')
#Styling the label widget
lbl2=Label(root, font=('Helvetica',20,'bold'), background='black', foreground='white')
lbl3=Label(root, font=('Calibri',15,'bold'), background='black', foreground='white')

lbl.pack()
lbl2.pack()
lbl3.pack()

time() 

quote()

mainloop()