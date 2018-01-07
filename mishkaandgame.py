n=int(raw_input())
m=0
c=0
for i in range(0,n):
	word=raw_input()
	l=map(int,word.split())
	if(l[0]>l[1]):
		m=m+1
	elif(l[0]<l[1]):
		c=c+1
if(m>c):
	print "Mishka"
elif(m<c):
	print "Chris"
else:
	print "Friendship is magic!^^"					