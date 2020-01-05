a1,b1=map(int,input().split())
b=1
while(b<=a1 and b<=b1):
	if(a1%b==0 and b1%b==0):
		C=b
	b=b+1
print(C)
	
