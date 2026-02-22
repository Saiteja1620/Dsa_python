##Intution
#1) convert the sentence of list of words
#2) using two pointer method (left pointer at 0, right pointer at length of the list) and value swap using a extra variable
#3) swap value at each pointer, until left pointer is less than right pointer.
#4) join the list of strings with space to form the sentence.

##Complexity
# If n is number of words in the sentence
#Time Complexity
#then this shall take O(log n) to swap all the words from left to right.

#Space Complexity
# O(n)

class Reverse:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        i,j=0,len(s)-1
        while i<j:
            t=s[i]
            s[i]=s[j]
            s[j]=t
            i+=1
            j-=1
        return ' '.join(s)
r=Reverse()
s=input('Enter sentence, in which words are to be reversed \n')
print(r.reverseWords(s))