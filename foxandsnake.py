import sys
r,c=map(int,sys.stdin.readline().split())
l1=["#"]*(c)
s1=''.join(map(str,l1))
l2=['.']*(c-1)
l2.append('#')
s2=''.join(map(str,l2))
l3=['.']*(c-1)
l3.insert(0,'#')
s3=''.join(map(str,l3))
i=0
while(i<r):
	if(i<r):
		print s1
		i=i+1
	if(i<r):
		print s2
		i=i+1
	if(i<r):
		print s1
		i=i+1
	if(i<r):
		print s3
		i=i+1			
			