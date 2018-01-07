def gcd(a, b):
    if a > b and b!=0:
        r=a%b
        if r == 0:
            return b
        else:
            return gcd(b, r)
    elif a < b and a!=0:
        r=b%a
        if r == 0:
            return a
        else:
            return gcd(a, r)
    else:
        return a
word=raw_input()
l=map(int,word.split())
a=l[0]
b=l[1]
n=l[2]
while(n>0):
    
    if(n-gcd(a,n)<0):
        print 1
        break
    elif(n-gcd(a,n)==0):
        print 0
        break
        
    else:
        n=n=n-gcd(a,n)    
    
    if (n-gcd(b,n)<0):
        print 0
        break
    elif(n-gcd(b,n)==0):
        print 1
        break    
    else:
        n=n-gcd(b,n)    
               
