import numpy as np
import os
import itertools
import Image as im
import re
from Tkinter import *

conditions=[]
cell_lines=[]
replicates=[]

root = Tk()
root.wm_title("Plateplanner V0.401")

## functions

def update_table():
	x=econditions.get()
	conditions.append(x)
	econditions.delete(0,END)
	con.insert(END,conditions[-1] + '\n')
	con.pack()
	cl.pack()
	rep.pack()

def reset_table():
	con.delete('1.0',END)
	conditions[:]=[]

def update_celllinestable():
	y=ecelllines.get()
	cell_lines.append(y)
	ecelllines.delete(0,END)
	cl.insert(END,cell_lines[-1] + '\n')
	cl.pack()
	con.pack()
	rep.pack()

def reset_celllinestable():
	cl.delete('1.0',END)
	cell_lines[:]=[]

def update_replicatestable():
	rep.delete('1.0',END)
	replicates[:]=[]
	z=ereplicates.get()
	replicates.append(z)
	ereplicates.delete(0,END)
	rep.insert(END,replicates[-1] + '\n')
	rep.pack()
	cl.pack()
	con.pack()

#frames

rowConditions = Frame(root)
rowConditions.grid(row=0, column=0, padx=10, pady=2)

conditionsleftFrame = Frame(rowConditions)
conditionsleftFrame.grid(row=0, column=0, padx=10, pady=2)

conditionsrightFrame = Frame(rowConditions)
conditionsrightFrame.grid(row=0, column=1, padx=10, pady=2)

rowcelllines = Frame(root)
rowcelllines.grid(row=1, column=0, padx=10, pady=2)

celllinesleftFrame = Frame(rowcelllines)
celllinesleftFrame.grid(row=0, column=0, padx=10, pady=2)

celllinesrightFrame = Frame(rowcelllines)
celllinesrightFrame.grid(row=0, column=1, padx=10, pady=2)

rowoptions = Frame(root)
rowoptions.grid(row=2, column=0, padx=10, pady=2)

rowoptionsleftFrame = Frame(rowoptions)
rowoptionsleftFrame.grid(row=0, column=0, padx=10, pady=2)

rowoptionsrightFrame = Frame(rowoptions)
rowoptionsrightFrame.grid(row=0, column=1, padx=10, pady=2)

### Enter Conditions

lconditions = Label(conditionsleftFrame,text="Conditions")
lconditions.grid(row=0,column=0,padx=10,pady=2)

econditions = Entry(conditionsleftFrame,width=20)
econditions.grid(row=0,column=1,padx=10,pady=2)

con = Text(conditionsrightFrame,width=50,height=10)
con.grid(row=0,column=0,padx=10,pady=2)

# Update button
Button(conditionsleftFrame, text='Add and Update', command=update_table).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# Reset button
Button(conditionsleftFrame, text='Reset', command=reset_table).grid(row=0,column=4,sticky=W,padx=10,pady=2)

### Enter Cell Types

lcelllines = Label(celllinesleftFrame,text="Cell types")
lcelllines.grid(row=1,column=0,padx=10,pady=2)

ecelllines = Entry(celllinesleftFrame,width=20)
ecelllines.grid(row=1,column=1,padx=10,pady=2)

cl = Text(celllinesrightFrame,width=50,height=10)
cl.grid(row=1,column=0,padx=10,pady=2)

Button(celllinesleftFrame, text='Add and Update', command=update_celllinestable).grid(row=1,column=3,sticky=W,padx=10,pady=2)

Button(celllinesleftFrame, text='Reset', command=reset_celllinestable).grid(row=1,column=4,sticky=W,padx=10,pady=2)

# replicates Dropdown menu

lreplicates = Label(rowoptionsleftFrame,text="Replicates")
lreplicates.grid(row=0,column=0,padx=10,pady=2)

ereplicates = Entry(rowoptionsleftFrame,width=20)
ereplicates.grid(row=0,column=1,padx=10,pady=2)

rep = Text(rowoptionsrightFrame,width=50,height=10)
rep.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionsleftFrame, text='Add and Update', command=update_replicatestable).grid(row=0,column=3,sticky=W,padx=10,pady=2)



#imagedisplay

bottomFrame = Frame(root)
bottomFrame.grid(row=4, column=0, padx=10, pady=2)

imageEx = PhotoImage(file = 'output.gif')
Label(bottomFrame, image=imageEx).grid(row=1, column=0, padx=10, pady=2)



# Exit button
Button(root, text='Exit', command=root.quit).grid(row=5,column=4,sticky=W,padx=10,pady=2)


root.mainloop()

print conditions
for item in conditions:
	print item

print cell_lines
for item in cell_lines:
	print item

print replicates
for item in replicates:
	print item
