A=int(input())
if A>1:
	for B in range(2,A):
		if(A%B==0):
			print("no")
			break
	else:
		    print("yes")
else:
	        print("no")
