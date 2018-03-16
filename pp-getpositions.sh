circle_size=20
D=20
circle_radius=10
R=10
x=("1" "2" "3")
y=("1" "2" "3")

for i in $x
do
x_pos=$("$i"*"$D"-"$R")
echo $x_pos
done