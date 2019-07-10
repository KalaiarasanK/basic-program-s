ab,bc=map(int,input().split())
A=ab*bc
for i in range(0,A+1):
	if(i**2==0):
		print("yes")
		break
else:
	print("no")
