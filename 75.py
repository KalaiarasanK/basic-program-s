kal=list(input())
if len(kal)%2==0:
	kal[int(len(kal)/2)]='*'
	kal[int(len(kal)/2)-1]='*'
else:
	kal[int(len(kal)/2)]='*'
for i in range(0,len(kal)):
	print(kal[i],end='')
