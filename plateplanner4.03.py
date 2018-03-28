import numpy as np
import os
import itertools
import re
from Tkinter import *

conditions=[]
cell_lines=[]

root = Tk()
root.wm_title("Plateplanner V0.403")

## functions

def update_table():
	x=econditions.get()
	conditions.append(x)
	econditions.delete(0,END)
	con.insert(END,conditions[-1] + '\n')
	con.pack()
	cl.pack()
	rep.pack()
	#yoff.pack()

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
	#yoff.pack()

def reset_celllinestable():
	cl.delete('1.0',END)
	cell_lines[:]=[]

def update_replicatestable():
	z=ereplicates.get()
	print z
	global replicates
	replicates=int(z)
	rep.delete('1.0',END)
	rep.insert(END,replicates)
	rep.pack()
	cl.pack()
	con.pack()
	#yoff.pack()

#def update_yoffsettable():
#	a=eyoffset.get()
#	print a
#	global yoffset
#	yoffset=int(a)
#	yoff.delete('1.0',END)
#	yoff.insert(END,yoffset)
#	yoff.pack()
#	cl.pack()
#	con.pack()
#	rep.pack()

def generate_image():
	cell_type_offset=40
	condition_offset=20
	n=0
	for i in conditions:
		n=(n+1)
		print "condition",n,":",i
	print "condition",n,":",i
	cell_types=cell_lines
	n=0
	for i in cell_types:
		n=(n+1)
		print "cell type",n,":",i
	number_of_duplicates=replicates
	print "number of dulplicates:",number_of_duplicates
	number_of_conditions=len(conditions)
	number_of_cell_types=len(cell_types)
	x_plates=number_of_conditions * number_of_duplicates
	print "mumner of columns:",x_plates
	y_plates=number_of_cell_types
	print "number of rows:",y_plates
	total_plates=x_plates * y_plates
	print "total plates:",total_plates
	xx=range(total_plates)
	xx = [n+1 for n in xx]
	xy=np.reshape(xx,(y_plates,x_plates))
	print "plate numbers in a linear array:\n",xx
	print "plate numbers in a matrix:\n",xy
	r=10 #radius
	d=20 #diameter
	diameter=d
	xc=range(x_plates)
	xc = [(((n+1)*d)-r) for n in xc]
	xc=np.tile(xc,(y_plates,1))
	xc=xc+cell_type_offset
	print "x coordinate matrix\n",xc
	xtc=xc
	print "x text coordinate matrix\n",xtc
	yc=range(y_plates)
	yc = [(((n+1)*d)-r) for n in yc]
	yc=np.tile(yc,(x_plates,1))
	yc=np.transpose(yc)
	yc=yc+condition_offset
	print "y coordinate matrix\n",yc
	ytc=yc+yoffset
	print "y text coordinate matrix\n",ytc
	# new matrix for treatments
	#trx=conditions*2 #not this
	trx=[ item for item in conditions for repetitions in range(number_of_duplicates) ] 
	trxy=np.tile(trx,(y_plates,1))
	print "treatment matrix:\n",trxy
	# new matrix for cell types
	#trx=conditions*2 #not this
	ct=cell_types
	print ct
	cty=np.tile(ct,(x_plates,1))
	ctxy=np.transpose(cty)
	print "cell type matrix:\n",ctxy
	#os.remove("image.svg")
	y=0
	for n in np.nditer(ctxy, order='C'):
		y=(y+1)
        	print(n)
		print(y)
	for tr,ct in itertools.izip(trxy,ctxy):
    		print(tr,ct)
	fi=open("output.svg","w")
	fi.write("<svg>\n")
	for n in xx:
		row,col = np.where(xy == n)
		name=xy[row,col]
		name=str(name)[1:-1]
		print name
		number=xy[row,col]
		number=str(number)[1:-1]
		print name
		xcoord1=xc[row,col]
		xcoord1=str(xcoord1)[1:-1]
		print xcoord1
		ycoord1=yc[row,col]
		ycoord1=str(ycoord1)[1:-1]
		print ycoord1
		xcoord2=xtc[row,col]
		xcoord2=str(xcoord2)[1:-1]
		print xcoord2
		ycoord2=ytc[row,col]
		ycoord2=str(ycoord2)[1:-1]
		print ycoord2
		radius1=str(r)
		print radius1
		celltype1=ctxy[row,col]
		celltype1=str(celltype1)[1:-1]
		print celltype1
		treatmenttype1=trxy[row,col]
		treatmenttype1=str(treatmenttype1)[1:-1]
		print treatmenttype1
		fa=open("template.t","r")
		for line in fa:
			a=re.compile('[N][A][M][E]')
			line = a.sub(name,line)
			print line
			b=re.compile('[X][C][O][O][R][D][1]')
			line = b.sub(xcoord1,line)
			print line
			c=re.compile('[X][C][O][O][R][D][2]')
			line = c.sub(xcoord2,line)
			print line
			d=re.compile('[Y][C][O][O][R][D][1]')
			line = d.sub(ycoord1,line)
			print line
			e=re.compile('[Y][C][O][O][R][D][2]')
			line = e.sub(ycoord2,line)
			print line
			f=re.compile('[N][U][M][B][E][R][1]')
			line = f.sub(number,line)
			print line
			g=re.compile('[R][A][D][I][U][S][1]')
			line = g.sub(radius1,line)
			print line
			fi.write(line)
		fa.close()
	#header rectangles
	trrl=diameter*number_of_duplicates
	trrl=str(trrl)
	print "trrl",trrl
	trrh=diameter
	trrh=str(trrh)
	print "trrh",trrh
	conditions2=list(conditions)
	print "conditions as list\n",conditions2
	conditions2.insert(0, '')
	print "conditions as list with blank first row (conditions2) \n",conditions2
	noc2=number_of_conditions
	vv=range(noc2+1)
	vv= [x*40 for x in vv]
	print "x coordinates for rectangles (vv)\n",vv
	YCOORD1=0
	YCOORD1=str(YCOORD1)
	#Y-offset of condition label text
	YCOORD2=15
	ycoord2=str(YCOORD2)
	for y in conditions2:
		col=conditions2.index(y)
		name=y
		name=str(name)
		xcoord1=vv[col]
		xcoord1=str(xcoord1)
		xcoord2=vv[col]+20
		xcoord2=str(xcoord2)
		fb=open("template2.t","r")
		for line in fb:
			a=re.compile('[N][A][M][E]')
			line=a.sub(name,line)
			b=re.compile('[T][R][R][L][1]')
			line=b.sub(trrl,line)
			c=re.compile('[T][R][R][H][1]')
			line=c.sub(trrh,line)
			d=re.compile('[X][C][O][O][R][D][1]')
			line = d.sub(xcoord1,line)
			e=re.compile('[Y][C][O][O][R][D][1]')
			line = e.sub(YCOORD1,line)
			f=re.compile('[X][C][O][O][R][D][2]')
			line = f.sub(xcoord2,line)
			g=re.compile('[Y][C][O][O][R][D][2]')
			line = g.sub(ycoord2,line)
			fi.write(line)
		fb.close()
	cell_types2=list(cell_types)
	print "cell types as list\n",cell_types2
	cell_types2.insert(0, '')
	print "cell types as list with blank first row (cell_types2)\n",cell_types2
	noct2=number_of_cell_types
	ww=range(noct2+1)
	ww=[x*20 for x in ww]
	print "y coordinates for rectangles (ww)\m",ww
	XCOORD1=0
	xcoord1=str(XCOORD1)
	#x offset - 50% rectangle diameter!
	XCOORD2=20
	xcoord2=str(XCOORD2)
	#y offset correction
	celltypeyoffset=15
	for y in cell_types2:
		col=cell_types2.index(y)
		name=y
		name=str(name)
		ycoord1=ww[col]
		ycoord1=str(ycoord1)
		ycoord2=ww[col]+celltypeyoffset
		ycoord2=str(ycoord2)
		fc=open("template3.t","r")
		for line in fc:
			a=re.compile('[N][A][M][E]')
			line=a.sub(name,line)
			b=re.compile('[T][R][R][L][1]')
			line=b.sub(trrl,line)
			c=re.compile('[T][R][R][H][1]')
			line=c.sub(trrh,line)
			d=re.compile('[X][C][O][O][R][D][1]')
			line = d.sub(xcoord1,line)
			e=re.compile('[Y][C][O][O][R][D][1]')
			line = e.sub(ycoord1,line)
			f=re.compile('[X][C][O][O][R][D][2]')
			line = f.sub(xcoord2,line)
			g=re.compile('[Y][C][O][O][R][D][2]')
			line = g.sub(ycoord2,line)
			fi.write(line)
		fc.close()
	fi.write("</svg>")
	fi.close()
	os.system("convert output.svg output.gif")
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

rowoptionsFrame1 = Frame(rowoptions)
rowoptionsFrame1.grid(row=0, column=0, padx=10, pady=2)

rowoptionsFrame2 = Frame(rowoptions)
rowoptionsFrame2.grid(row=1, column=0, padx=10, pady=2)

rowoptionsFrame3 = Frame(rowoptions)
rowoptionsFrame3.grid(row=2, column=0, padx=10, pady=2)

rowoptionsFrame4 = Frame(rowoptions)
rowoptionsFrame4.grid(row=3, column=0, padx=10, pady=2)

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

lreplicates = Label(rowoptionsFrame1,text="Replicates")
lreplicates.grid(row=0,column=0,padx=10,pady=2)

ereplicates = Entry(rowoptionsFrame1,width=5)
ereplicates.grid(row=0,column=1,padx=10,pady=2)

rep = Text(rowoptionsFrame1,width=5,height=1)
rep.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionsFrame1, text='Add and Update', command=update_replicatestable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# yoffset Dropdown menu

#lyoffset = Label(rowoptionsFrame2,text="Text Y Offset")
#lyoffset.grid(row=0,column=0,padx=10,pady=2)

#eyoffset = Entry(rowoptionsFrame2,width=5)
#eyoffset.grid(row=0,column=1,padx=10,pady=2)

#yoff = Text(rowoptionsFrame2,width=5,height=1)
#yoff.grid(row=0,column=2,padx=10,pady=2)

#Button(rowoptionsFrame2, text='Add and Update', command=update_yoffsettable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

#imagedisplay

bottomFrame = Frame(root)
bottomFrame.grid(row=4, column=0, padx=10, pady=2)

Button(bottomFrame, text='Generate Image', command=generate_image).grid(row=1,column=2,sticky=W,padx=10,pady=2)

# Exit button
Button(root, text='Exit', command=root.quit).grid(row=5,column=4,sticky=W,padx=10,pady=2)


root.mainloop()
