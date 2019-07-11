num=list(input())
num1=[]
for i in num:
	if i not in num1:
		num1.append(i)
if num==num1:
	print("Yes")
else:
	print("No")
