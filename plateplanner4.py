import numpy as np
import os
import itertools
import re
from Tkinter import *

conditions=[]
cell_lines=[]
replicates=[]

root = Tk()
root.wm_title("Plateplanner V0.4")

def update_table():
	x=econditions.get()
	conditions.append(x)
	var.set(x)	
	econditions.delete(0,END)
	t.insert(END,conditions[-1] + '\n')
	t.pack()

def reset_table():
	t.delete('1.0',END)
	conditions[:]=[]

var = StringVar()

leftFrame = Frame(root,width=200,height=600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

lconditions = Label(leftFrame,text="Conditions")
lconditions.grid(row=0,column=0,padx=10,pady=2)

econditions = Entry(leftFrame,width=10)
econditions.grid(row=0,column=1,padx=10,pady=2)

#aconditions = Button(leftFrame, text='add', command=append_condition)
#aconditions.grid(row=0,column=2,sticky=W,padx=10,pady=2)

rightFrame = Frame(root,width=200,height=600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)

t = Text(rightFrame)
t.grid(row=0,column=1,padx=10,pady=2)

#def update_table():
#	label.config(text=("\n".join(conditions)))


#def update_table():
#	t.insert(END,conditions[-1] + '\n')
#	t.pack()

#def update_table():
#	for item in conditions:
#		t.insert(END,item + '\n')
#	t.pack()


# Update button
Button(leftFrame, text='Add and Update', command=update_table).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# Reset button
Button(leftFrame, text='Reset', command=reset_table).grid(row=0,column=4,sticky=W,padx=10,pady=2)

# Exit button
Button(leftFrame, text='Exit', command=root.quit).grid(row=5,column=5,sticky=W,padx=10,pady=2)


root.mainloop()

print conditions

for item in conditions:
	print item
