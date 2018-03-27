import numpy as np
import os
import itertools
import re
#import Tkinter as tk
from Tkinter import *
#import svgwrite

root = Tk()
root.wm_title("Plateplanner V0.3") #title the window
root.config(background = "#FFFFFF") #background colour

leftFrame = Frame(root, width=200, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)

firstLabel = Label(leftFrame, text="Plating Options")
firstLabel.grid(row=0, column=0, padx=10, pady=2)

entry1 = Entry(leftFrame,width=10)
entry1.grid(row=1,column=1,padx=10,pady=2)
entry1.get()

Button(leftFrame, text='input', command=root.quit).grid(row=1,column=2,sticky=W,padx=10,pady=2)

secondLabel = Label(leftFrame, text="Enter Number of Conditions")
secondLabel.grid(row=1, column=0, padx=10, pady=2)

entry2 = Entry(leftFrame,width=10)
entry2.grid(row=2,column=1,padx=10,pady=2)
entry2.get()

thirdLabel = Label(leftFrame, text="Number of cell lines")
thirdLabel.grid(row=2, column=0, padx=10, pady=2)

Button(leftFrame, text='input', command=root.quit).grid(row=2,column=2,sticky=W,padx=10,pady=2)

entry3 = Entry(leftFrame,width=10)
entry3.grid(row=3,column=1,padx=10,pady=2)
entry3.get()

thirdLabel = Label(leftFrame, text="Number of Technical Replicates")
thirdLabel.grid(row=3, column=0, padx=10, pady=2)

Button(leftFrame, text='input', command=root.quit).grid(row=3,column=2,sticky=W,padx=10,pady=2)


Button(leftFrame, text='Exit', command=root.quit).grid(row=4,column=0,sticky=W,padx=10,pady=2)

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (entry1.get(), entry2.get()))
   x = entry1.get()
   y = entry2.get()
   z = entry3.get()
Button(leftFrame, text='Show', command=show_entry_fields).grid(row=4, column=1, sticky=W, pady=4)




#Right Frame and its contents
rightFrame = Frame(root, width=200, height = 600)
rightFrame.grid(row=0, column=1, padx=10, pady=2)


imageEx = PhotoImage(file = 'output.gif')
Label(rightFrame, image=imageEx).grid(row=1, column=0, padx=10, pady=2)

root.mainloop() #monitor the window

# Enter statistics
yoffset=4
cell_type_offset=40
condition_offset=20

conditions=("DMSO","991","2DG")
n=0
for i in conditions:
	n=(n+1)
	print "condition",n,":",i

print "condition",n,":",i

cell_types=("WT","LKB1")
n=0
for i in cell_types:
	n=(n+1)
	print "cell type",n,":",i

number_of_duplicates=2
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

