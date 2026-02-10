##Problem Statement:
#Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

##Intution
#Two pointer method
#1) if length of input is greater than 10, initialize i at 0, j at 10th index.
#2) Take every i:j string and count if it has occurred or not using a dictionary
#3) Increment i,j by one, after each iteration.
#4) if j becomes greater than len of the input, then return sub strings which has occured more than once.

###Complexity

##Time Complexity
#if length is 10 - O(1)
#if length is 13 - O(4) as we consider 3 strings, 0-10, 1-11, 2-12, 3-13
#So O(n+1) for adding patterns, another O(n+1) to check and print the patterns , where n is length of the string.

##Space Complexity
#result list - O(n+1)
#validPattersn - O(n+1)
#Total - O(2n+2) => O(n)  where n=len(s)/10


s=input('Enter any DNA Pattern \n')

#1
if len(s)>=10:
    dna=list('ACGT')
    result,pattern,validPatterns,i,j=[],'',{},0,10
    while i<j:
        #2
        #O(n+1)
        pattern=s[i:j]
        if pattern not in validPatterns:
            validPatterns[pattern]=1
        elif pattern in validPatterns or pattern[::-1] in validPatterns:
            validPatterns[pattern]+=1
        
        #3
        i+=1
        j+=1

        #4
        if j>len(s):
            for k in validPatterns:
                if validPatterns[k]>1:
                    result.append(k)
            print(result)
            exit(0)
else:
    print([])