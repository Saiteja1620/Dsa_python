##Intution
#1) Find the least length string, because max common prefix would be of length, least string in the list
#2) Trim the rest of the strings in the list, to have same length like least string.
#3) Iterate over the least string, if a character in it is not matching with one of the string, then that character is not meant to be added to common string.
#4) If that character is present in all the strings, then that has to be kept tracked, when iteration is done, should be added to common.

strs=list(input('Enter list of strings to find longest common prefix').split())
common=''
leastLength=9999
leastString=''

#if length of the list is one, then longest common prefix would be itself.
if(len(strs))==1:
    print('Longest common prefix is itself', strs[0])
    exit(0)

#1
for i in strs:
    if len(i)<leastLength:
        leastLength=len(i)
        leastString=i
# strs.remove(leastString)

#2
strs=list(map(lambda x: x[:leastLength],strs))

#3
present=False
for i in range(len(leastString)):
    track='' 
    #4   
    for j in strs:
        if leastString[i]!=j[i]:
            break
        else:
            present=True
            track=leastString[i]
    if present:
        common+=track
print(f'Longest Common prefix among the list of strings is', common)