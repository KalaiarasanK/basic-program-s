num1,num2=map(int,input().split())
char=input().split()
a=[]
for i in char:
	if(int(i)%2!=0):
		a.append(i)
print(a[num2-1])
