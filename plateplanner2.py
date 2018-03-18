import numpy as np
import os
import itertools
import re
#import svgwrite

# Enter statistics
conditions=("DMSO","991","2DG","PHEN")
n=0
for i in conditions:
	n=(n+1)
	print "condition",n,":",i

print "condition",n,":",i

cell_types=("WT","AXIN","LKB1","900")
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

xc=range(x_plates)
xc = [(((n+1)*d)-r) for n in xc]
xc=np.tile(xc,(y_plates,1))
print "x coordinate matrix\n",xc
yc=range(y_plates)
yc = [(((n+1)*d)-r) for n in yc]
yc=np.tile(yc,(x_plates,1))
yc=np.transpose(yc)
print "y coordinate matrix\n",yc

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

i=open("output.svg","w")
i.write("<svg>\n")

for n in np.nditer(ctxy,order='C'):


f=open("template.t","r")
for line in f:
	line=


	i.write(line)

f.close()
i.write("<\svg>")
i.close()