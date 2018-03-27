import numpy as np
import os
import itertools
import re
from Tkinter import *

conditions=["DMSO","991"]
cell_lines=[]
replicates=[]

root = Tk()
root.wm_title("Plateplanner V0.4")

var = StringVar()

def append_condition():
	x=econditions.get()
	conditions.append(x)
	var.set(x)	
	econditions.delete(0,END)

leftFrame = Frame(root,width=200,height=600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

lconditions = Label(leftFrame,text="Conditions")
lconditions.grid(row=0,column=0,padx=10,pady=2)

econditions = Entry(leftFrame,width=10)
econditions.grid(row=0,column=1,padx=10,pady=2)

aconditions = Button(leftFrame, text='add', command=append_condition)
aconditions.grid(row=0,column=2,sticky=W,padx=10,pady=2)

t = Text(leftFrame)
t.grid(row=1,column=0,padx=10,pady=2)

#def update_table():
#	label.config(text=("\n".join(conditions)))


def update_table():
	for item in conditions:
		t.insert(END,item + '\n')
	t.pack()

var.trace('w',update_table)

# Exit button
Button(leftFrame, text='Exit', command=root.quit).grid(row=5,column=5,sticky=W,padx=10,pady=2)


root.mainloop()

print conditions

for item in conditions:
	print item
