import math
k=list(map(int,input().split()))
for i in k:
	print(int((k[0]*k[1])/math.gcd(k[0],k[1])))
	break
