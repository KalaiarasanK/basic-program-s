num=int(input())
a=0
i=0
while(num):
	i=num%10
	a=a+i
	num=num//10
print(a)	
