a=int(input())
b=int(input())
c=int(input())

s=a+b*c
t= a*(b+c)
u=a*b*c
v=(a+b)*c
w=a+b+c

max=s
if(max<t):
	max=t
if(max<u):
	max=u

if(max<v):
	max=v
if(max<w):
	max=w	

print max	
