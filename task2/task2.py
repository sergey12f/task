import os

cy = 1
cx = 1
r= 5
py = 6
px = 6
def point_position(cy,cx,r,py,px):
	if (py-cy)**2+(px-cx)**2<=r**2:
		if (py-cy)**2+(px-cx)**2==r**2:
			print(0)
		else:
			print(1)
	else:
		print(2)

current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)
with open(current_directory+'/circle.txt','r') as file:
	clist = list(file)
with open(current_directory+'/point.txt','r') as file:
	plist = list(file)
for i in range(len(plist)):
	point_position(int(clist[0][0]),int(clist[0][2]),int(clist[1][0]),int(plist[i][0]),int(plist[i][2]))

