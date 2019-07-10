i=0
A,B=map(int,input().split())
C=list(map(int,input().split()))[:A]
for k in C:
	if k==B:
		i+=1
if(i!=0):
	print("yes")
else:
	print("no")
