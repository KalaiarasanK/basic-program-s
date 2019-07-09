a,b=map(int,input().split())
for i in range(a+1,b):
	sum=0
	num=i
	while num>0:
		dig=num%10
		sum+=dig**3
		num//=10
		if(i==sum):
			print(i,end=" ")
