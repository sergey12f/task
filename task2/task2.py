def point_position(cy,cx,r,py,px):
	if (py-cy)**2+(px-cx)**2<=r**2:
		if (py-cy)**2+(px-cx)**2==r**2:
			print(0)
		else:
			print(1)
	else:
		print(2)
with open(input('путь к файлу с координатами круга в формате:C:/circle.txt\n'),'r') as file:
	clist = list(file)
with open(input('путь к файлу с координатами точек в формате:C:/point.txt\n'),'r') as file:
	plist = list(file)
for i in range(len(plist)):
	point_position(int(clist[0][0]),int(clist[0][2]),int(clist[1][0]),int(plist[i][0]),int(plist[i][2]))

