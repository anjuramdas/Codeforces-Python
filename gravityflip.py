n=int(raw_input())
word=raw_input()
l=map(int,word.split())
m=[]
m=sorted(l)
j=max(l)
while(j>=0):

	for i in range(0,n-1):
		if(l[i]>=l[i+1]):
			l[i]=l[i]-1
			l[i+1]=l[i+1]+1
		
	if(l==m):
		break
	else:
		j=j-1

for i in range(0,n):
	print l[i],