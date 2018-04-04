import numpy as np
import os
import sys
import itertools
import re
from Tkinter import *
from PIL import Image, ImageTk

conditions=[]
cell_lines=[]

#default values

radius=10
diameter=20
ctyoffset=20
ctxoffset=40
yoff=4
replicates=2


root = Tk()
root.wm_title("Plateplanner V0.404")

## functions

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def update_table():
	x=econditions.get()
	conditions.append(x)
	econditions.delete(0,END)
	con.insert(END,conditions[-1] + '\n')
	con.pack()
	cl.pack()
	rep.pack()
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()

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
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()

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
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()

def update_yoffsettable():
	a=eyoffset.get()
	print a
	global yoffset
	yoffset=int(a)
	yoff.delete('1.0',END)
	yoff.insert(END,yoffset)
	rep.pack()
	cl.pack()
	con.pack()
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()

def update_ctxoffsettable():
	b=ectxoffset.get()
	print b
	global ctxoffset
	ctxoffset=int(b)
	global condition_offset
	condition_offset=ctxoffset
	ctxoff.delete('1.0',END)
	ctxoff.insert(END,ctxoffset)
	rep.pack()
	cl.pack()
	con.pack()
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()

def update_ctyoffsettable():
	c=ectyoffset.get()
	print c
	global ctyoffset
	ctyoffset=int(c)
	global cell_type_offset
	cell_type_offset=ctyoffset
	ctyoff.delete('1.0',END)
	ctyoff.insert(END,ctyoffset)
	rep.pack()
	cl.pack()
	con.pack()
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()


def update_radiustable():
	d=eradius.get()
	print d
	global radius
	radius=int(d)
	global rad
	rad=radius
	rds.delete('1.0',END)
	rds.insert(END,radius)
	rep.pack()
	cl.pack()
	con.pack()
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()

def update_diametertable():
	e=eradius.get()
	print e
	global diameter
	diameter=int(e)
	global dia
	dia=diameter
	dtr.delete('1.0',END)
	dtr.insert(END,radius)
	rep.pack()
	cl.pack()
	con.pack()
	yoff.pack()
	ctxoff.pack()
	ctyoff.pack()
	rds.pack()
	dtr.pack()



def show_blankimage():
	im=Image.open("output.gif")
	width, height = im.size
	load=Image.open("blank.gif")
	load=load.resize((im.size),Image.NEAREST)
	render=ImageTk.PhotoImage(load)
	img=Label(bottomFrame2,image=render)
	img.image=render
	img.place(x=0,y=0)


def show_image():
	load=Image.open("output.gif")
	render=ImageTk.PhotoImage(load)
	img=Label(bottomFrame2,image=render)
	img.image=render
	img.place(x=0,y=0)

def generate_image():
	cell_type_offset=ctyoffset
	condition_offset=ctxoffset
	yoffset=yoff
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
	number_of_conditions=len(conditions)
	number_of_cell_types=len(cell_types)
	x_plates=number_of_conditions * number_of_duplicates
	y_plates=number_of_cell_types
	total_plates=x_plates * y_plates
	xx=range(total_plates)
	xx = [n+1 for n in xx]
	xy=np.reshape(xx,(y_plates,x_plates))
	r=radius #radius
	print r
	print radius
	d=2*r #diameter
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
	yoff=int(yoff)	
	ytc=yc+yoff
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
	#vv= [x*40 for x in vv]
	dv=int(diameter)
	vv= [x*dv for x in vv]
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
	#ww=[x*20 for x in ww]
	wr=int(radius)
	ww=[x*wr for x in ww]
	print "y coordinates for rectangles (ww)\m",ww
	XCOORD1=0
	xcoord1=str(XCOORD1)
	#x offset - 50% rectangle diameter!
	XCOORD2=radius
	xcoord2=str(XCOORD2)
	#y offset correction /// INPUT "CONDITION LABEL DODGE"
	celltypeyoffset=ctyoffset
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

rowoptionsfirstleftFrame = Frame(rowoptions)
rowoptionsfirstleftFrame.grid(row=0, column=0, padx=10, pady=2)
rowoptionsfirstrightFrame = Frame(rowoptions)
rowoptionsfirstrightFrame.grid(row=0, column=1, padx=10, pady=2)

rowoptionssecondleftFrame = Frame(rowoptions)
rowoptionssecondleftFrame.grid(row=1, column=0, padx=10, pady=2)
rowoptionssecondrightFrame = Frame(rowoptions)
rowoptionssecondrightFrame.grid(row=1, column=1, padx=10, pady=2)

rowoptionsthirdleftFrame = Frame(rowoptions)
rowoptionsthirdleftFrame.grid(row=2, column=0, padx=10, pady=2)
rowoptionsthirdrightFrame = Frame(rowoptions)
rowoptionsthirdrightFrame.grid(row=2, column=1, padx=10, pady=2)

rowoptionsfourthleftFrame = Frame(rowoptions)
rowoptionsfourthleftFrame.grid(row=3, column=0, padx=10, pady=2)
rowoptionsfourthrightFrame = Frame(rowoptions)
rowoptionsfourthrightFrame.grid(row=3, column=1, padx=10, pady=2)

rowoptionsfifthleftFrame = Frame(rowoptions)
rowoptionsfifthleftFrame.grid(row=4, column=0, padx=10, pady=2)
rowoptionsfifthrightFrame = Frame(rowoptions)
rowoptionsfifthrightFrame.grid(row=4, column=1, padx=10, pady=2)

rowoptionssixthleftFrame = Frame(rowoptions)
rowoptionssixthleftFrame.grid(row=5, column=0, padx=10, pady=2)
rowoptionssixthrightFrame = Frame(rowoptions)
rowoptionssixthrightFrame.grid(row=5, column=1, padx=10, pady=2)


canvas1 = Frame(root)
canvas1.grid(row=3, column=0, padx=10, pady=2)

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

# replicates entry

lreplicates = Label(rowoptionsfirstleftFrame,text="Replicates",width=30)
lreplicates.grid(row=0,column=0,padx=10,pady=2)

ereplicates = Entry(rowoptionsfirstleftFrame,width=5)
ereplicates.grid(row=0,column=1,padx=10,pady=2)

rep = Text(rowoptionsfirstrightFrame,width=5,height=1)
rep.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionsfirstleftFrame, text='Add and Update', command=update_replicatestable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# text y-offset entry

lyoffset = Label(rowoptionssecondleftFrame,text="Plate number label offset (4)",width=30)
lyoffset.grid(row=0,column=0,padx=10,pady=2)

eyoffset = Entry(rowoptionssecondleftFrame,width=5)
eyoffset.grid(row=0,column=1,padx=10,pady=2)


yoff = Text(rowoptionssecondrightFrame,width=5,height=1)
yoff.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionssecondleftFrame, text='Add and Update', command=update_yoffsettable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# cell type label adjustment

lctxoffset = Label(rowoptionsthirdleftFrame,text="Cell line label dodge (40)",width=30)
lctxoffset.grid(row=0,column=0,padx=10,pady=2)

ectxoffset = Entry(rowoptionsthirdleftFrame,width=5)
ectxoffset.grid(row=0,column=1,padx=10,pady=2)

ctxoff = Text(rowoptionsthirdrightFrame,width=5,height=1)
ctxoff.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionsthirdleftFrame, text='Add and Update', command=update_ctxoffsettable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# condition label adjustment

lctyoffset = Label(rowoptionsfourthleftFrame,text="Condition label dodge (20)",width=30)
lctyoffset.grid(row=0,column=0,padx=10,pady=2)

ectyoffset = Entry(rowoptionsfourthleftFrame,width=5)
ectyoffset.grid(row=0,column=1,padx=10,pady=2)

ctyoff = Text(rowoptionsfourthrightFrame,width=5,height=1)
ctyoff.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionsfourthleftFrame, text='Add and Update', command=update_ctyoffsettable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# radius adjustment

lradius = Label(rowoptionsfifthleftFrame,text="Radius (20)",width=30)
lradius.grid(row=0,column=0,padx=10,pady=2)

eradius = Entry(rowoptionsfifthleftFrame,width=5)
eradius.grid(row=0,column=1,padx=10,pady=2)

rds = Text(rowoptionsfifthrightFrame,width=5,height=1)
rds.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionsfifthleftFrame, text='Add and Update', command=update_radiustable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

# diameter adjustment

ldiameter = Label(rowoptionssixthleftFrame,text="Diameter (20)",width=30)
ldiameter.grid(row=0,column=0,padx=10,pady=2)

ediameter = Entry(rowoptionssixthleftFrame,width=5)
ediameter.grid(row=0,column=1,padx=10,pady=2)

dtr = Text(rowoptionssixthrightFrame,width=5,height=1)
dtr.grid(row=0,column=2,padx=10,pady=2)

Button(rowoptionssixthleftFrame, text='Add and Update', command=update_diametertable).grid(row=0,column=3,sticky=W,padx=10,pady=2)

#imagedisplay

#imageEx = PhotoImage(file = 'output.gif')
#Label(canvas1, image=imageEx).grid(row=1, column=0, padx=10, pady=2)

bottomFrame = Frame(root)
bottomFrame.grid(row=4, column=0, padx=10, pady=2)

bottomFrame2 = Frame(root,height=400,width=1024)
bottomFrame2.grid(row=5, column=0, padx=10, pady=2)

Button(bottomFrame, text='Generate Image', command=generate_image).grid(row=1,column=2,sticky=W,padx=10,pady=2)

Button(bottomFrame, text='Clear Image', command=show_blankimage).grid(row=1,column=3,sticky=W,padx=10,pady=2)

Button(bottomFrame, text='Show Image', command=show_image).grid(row=1,column=4,sticky=W,padx=10,pady=2)

# Exit button
Button(root, text='Exit', command=root.quit).grid(row=5,column=4,sticky=W,padx=10,pady=2)

Button(root, text='Restart', command=restart_program).grid(row=5,column=5,sticky=W,padx=10,pady=2)

root.mainloop()
