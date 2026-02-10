#Problem Statement: Given two strings, check if they form an anagram or not
#Anagram - letters of first string are jumbled and used to form the second word

##Intution
#Take count of each letter in first string in a dictionary
#if letter is present in second string as well, then subract the count.
#if any value is 1 or >1 in dictionary then, its not a anagram i.e. different letters are used in both the strings.
#if value is 0, then it is an anagram

##Complexity
#Time Complexity
#O(n+m) where n,m are length of the strings.

#Space Complexity
#O(n+m) where n,m are length of the strings - in worst case, I'll need to store elements of both the strings


s,t,=input('Enter string one \n'), input('Enter string two \n')
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in t:
    if i in d:
        d[i]-=1
    else:
        print( False)
        exit(0)
for i in d:
    if d[i]!=0:
        print( False)
        exit(0)
print( True)
exit(0)
