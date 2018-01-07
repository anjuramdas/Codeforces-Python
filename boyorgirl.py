import sets
name=raw_input()
#length=len(name)
#user=[]
user=''.join(set(name))

"""for i in range(0,length):
	for x in user:
		if(x==name[i]):
			break
	#user.append(name[i])"""		
l=len(user)
if(l%2==0):
	print"CHAT WITH HER!"
else:
	print"IGNORE HIM!"	
	

	