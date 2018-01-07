def bubblesort( m ):
	for i in range( len( m ) ):
		for k in range( len( m ) - 1, i, -1 ):
			if ( m[k] > m[k - 1] ):
				swap( m, k, k - 1 )
	return m 
def swap( A, x, y ):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp
n=int(raw_input())
if(n>=1 and n<=100):
	input=raw_input()
	l=input.split()
	m=[ int(x) for x in l ]
	length=len(m)
	s1=0
	#s2=0
	c=0
	"""size=(length-1)/2
	for i in range(0,size+1):
		s1=s1+m[i]
		c=c+1
	for i in range(size+1,length):
		s2=s2+m[i]
	if(s1>s2):
		print c
	else:
		s1=s1+m[size+1]
		print c+1"""
	p=bubblesort(m)
	#print p
	for i in range(0,length):
		s1=s1+p[i]
		#print s1
		c=c+1
		s2=0
		for j in range(i+1,length):
			
			s2=s2+p[j]
			#print s2
		if(s1>s2):
			print c
			break		