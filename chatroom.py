word=raw_input()
for i in range(0,len(word)):
	if(word[i]=='h'):
		for j in range(i+1,len(word)):
			if(word[j]=='e'):
				for k in range(j+1,len(word)):
					if(word[k]=='l'):
						for l in range(k+1,len(word)):
							if(word[l]=='l'):
								for m in range(l+1,len(word)):
									if(word[m]=='o'):
										print "YES"
										exit()
print "NO"										