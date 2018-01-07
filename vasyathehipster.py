import sys
a,b=map(int,sys.stdin.readline().split())
count=0
while(a>0 and b>0):
	a=a-1
	b=b-1
	count=count+1	
print count,
count=0	
while(a>1):
		a=a-2
		count=count+1
while(b>1):
		b=b-2
		count=count+1
print count					