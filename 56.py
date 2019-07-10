num=input()
count=0
for i in num:
	if(i.isdigit() or i.isalpha()):
	    count+=1
if count!=0:
	print("yes")
else:
	print("no")	
