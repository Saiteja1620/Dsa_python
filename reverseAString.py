s=list(input('Enter a string to reverse \n'))
i,j=0,len(s)-1
while i<=j:
    first=s[i]
    last=s[j]
    s[i]=last
    s[j]=first
    i+=1
    j-=1
print(s)