A=int(input())
B=[]
for i in range(1,A+1):
	if A%i == 0:
		B.append(str(i))
print(' '.join(B))
