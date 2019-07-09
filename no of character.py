num=input()
A=0
for i in range(len(num)):
	if(num[i].isdigit() or num[i].isalpha() or num[i]==(" ")):
		continue
	else:
		A+=1
print(A)		
