num1,num2=map(int,input().split()) 
maximum=max(num1,num2)
while(1):
	if(maximum%num1==0 and maximum%num2==0):
		print(maximum)
		break
maximum+=1
