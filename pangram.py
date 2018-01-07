n=int(raw_input())
word=raw_input()
word=word.lower()
if(n<26):
	print "NO"
else:
	l=[]
	for i in range(0,n):
		l.append(word[i])
	#print l
	k=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for j in k:
		if(l.count(j)<1):
			print"NO"
			exit()
	print"YES"		

