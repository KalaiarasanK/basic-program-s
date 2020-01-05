A,B,C=map(int,input().split())
num=0
for i in range(0,C):
	num=num+A
	A=A+B
print(num)	
