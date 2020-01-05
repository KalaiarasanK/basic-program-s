A = int(input())
num = list(map(int,input().split()))
for i in range(len(num)-1):
	if(num[i]>num[i+1]):
		print(i)
