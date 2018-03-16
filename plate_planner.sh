# Enter conditions
conditions=("DMSO" "991" "2DG" "PHEN")
cell_types=("WT" "KO" "KO2" "KO3")
number_of_duplicates=2

number_of_conditions=${#conditions[@]} # calculate number of different conditions from vector length
number_of_types=${#cell_types[@]} # count number of different cell types from vector length
x_plates=$(echo $(($number_of_conditions * $number_of_duplicates))) # calculate the number of plates in x-direction
y_plates=$(echo $(($number_of_types))) # calculate number of plates in y direction

echo "$x_plates plates per cell type" # display number in x direction
echo "$y_plates different cell types of isoforms" # display number in y direction

x=$(seq $x_plates) # make sequence vector for x
echo "plates in x direction:"
echo $x
y=$(seq $y_plates) # make sequence vector for y
echo "levels in y direction:"
echo $y

## loop to define row end max values
for a in $y
do
h=$(echo $(($a * $x_plates)))
x_max+=("$h")
done
echo "end row maximums:"
echo ${x_max[@]}

echo "set row 1 to e1:"
e1=$x
echo $e1

for b in $y
do
echo "row number"
echo "$b" #1 2 3
c1=$(($b-1))
echo "element number:"
echo "$c1"
eval er$b=${x_max["$c1"]}
done

containsElement () {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}

j=0
j2=1
for bmx in $y
do
for n in $e1 #1 2 3 4 5 6 7 8
do
j=$((j + 1))
nv=("$((n + er$bmx))")
o+=("$nv")
echo "ARRAY"
echo ${o[@]}
yn=$(containsElement "$j" "${x_max[@]}" && echo yes || echo no)
echo $yn
if [ $yn == "yes" ]
then
echo "hooray"
j2=$((j2 + 1))
min=${o[0]}
echo $min
max=${o[-1]}
echo $max
v=$(seq "$min" 1 "$max")
echo "thisisv"
echo $v
for vv in $v
do
eval "e$j2+=("$vv")"
done
o=()
fi
done 
done

echo ${e1[@]}
echo ${e2[@]}
echo ${e3[@]}
echo ${e4[@]}
echo ${e5[@]}

echo $y
rows=()
for r in $y
do
echo $r
rows+=("e$r")
done

echo ${rows[@]}
echo ${allrows[@]}

for f in ${rows[@]}
do
eval echo \${$f[@]}
done

circle_size=20
D=20
circle_radius=10
R=10

for i in ${x[@]};
do
#echo $i
eval a=$(echo "$[$i * $D - $R]")
#echo $a
x_coords+=("$a")
done

for i in ${y[@]};
do
#echo $i
eval a=$(echo "$[$i * $D - $R]")
#echo $a
y_coords+=("$a")
done

echo x_coords
echo ${x_coords[@]}
echo y_coords
echo ${y_coords[@]}

echo ${x_max[-1]}
plates=$(seq "${x_max[-1]}")
echo $plates


rm working.t
rm working2.t

echo "<svg>" >> working2.t

for i in $plates
do
cat "template.t" > working.t
sed -i s/NAME/"$i"/ working.t
sed -i s/NUMBER/"$i"/ working.t
sed -i s/LINEx/"$i"/ working.t
sed -i s/RADIUS/"$R"/ working.t

cat working.t >> working2.t
done

echo "<\svg>" >> working2.t

rm xcoords1.t
rm xcoords2.t

for run in ${x[@]}
do

for i in ${x_coords[@]}
do
echo $i >> xcoords1.t
echo $i >> xcoords2.t
done

done

i=0

echo ${y[@]}
rm ycoords.t

for i in ${e1[@]}
do
echo $(${y["$i"]}) >> ycoords.t
done





#rm working.t
#for i in $plates
#do
#cat "template.t" >> working.t
#eval $(echo "sed s/NAME/$i/ working.t")
#eval $(echo "sed s/NUMBER/$i/ working.t")
#cat working.t >> file.svg
#done
#echo "<\svg>" >> file.svg

#for i in $x_plates;
#do
#a=$(echo $(($i * $D - $R)))
#echo "
#  <g id="$i">
#    <circle style="fill:#FFFFFF; stroke:#000000; stroke-width:2" cx="$a" cy="12.5" r="12.5">
#    </circle>
#    <text x="12.5" y="12.5" fill="#000000" text-anchor="middle" font-size="14" font-family="'Arial'">1</text>
#  </g>"
#done