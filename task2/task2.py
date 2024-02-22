import sys
def point_position(cy,cx,r,py,px):
	if (py-cy)**2+(px-cx)**2<=r**2:
		if (py-cy)**2+(px-cx)**2==r**2:
			print(0)
		else:
			print(1)
	else:
		print(2)
with open(sys.argv[1],'r') as file:
	clist = list(file)
with open(sys.argv[2],'r') as file:
	plist = list(file)
for i in range(len(plist)):
	point_position(int(clist[0][0]),int(clist[0][2]),int(clist[1][0]),int(plist[i][0]),int(plist[i][2]))

