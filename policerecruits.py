n=int(raw_input())
word=raw_input()
count=0
pos=0

l=map(int,word.split())

for i in range(0,n):
	if(l[i]>0):
		pos=pos+l[i]
	elif(pos>0):
		pos=pos-1
	else:
		count=count+1


print count