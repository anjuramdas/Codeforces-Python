import sys
m,n=map(int,sys.stdin.readline().split())
s=m
while(m>=n):
	k=m%n
	m=m/n
	s=s+m
	m=m+k
print s