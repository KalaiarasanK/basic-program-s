a=int(input())
AB=a
sum=0
while a>0:
	B=a%10
	sum=sum+B*B*B
	a=a//10
if AB==sum:
	print("yes")
else:
	print("no")
