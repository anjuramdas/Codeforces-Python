word=raw_input()
length=len(word)
c=0
for i in range(0,length):
	if(word[i]=='H' or word[i]=='Q' or word[i]=='9'):
		print "YES"
		c=1
		break
if(c==0):
	print "NO"		