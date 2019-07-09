num1,num2=map(int,input().split())
for num3 in range(num1+1,num2):
	if(num3%2!=0):
		print(num3,end=" ")
