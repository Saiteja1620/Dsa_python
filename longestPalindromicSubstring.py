##Problem Statement
#Given a string, find out longest string which is also a palindrome.

##Intution
#two pointer method 
#1) if length of string is greater than 1, initialize i,j at 0,0.
#2) consider substring from i to j (using slicing), check if its a palindrome or not.
#3) increment j until it reaches length of string, if reaches, move i to next and initiliaze j to i (to consider new set of sub strings, from next character.)

#Its like first, you are finding out an palindrome, storing it, then when new substring is found, instead of direclty checking if
#its a Palindrome or not, we are checking length of new sub string is greater than the palindrome we already got, it yes, then 
#check if its Palindrome or not. This saves more than half of the time

##Complexity
#Space - O(n), string at max, holds every character in the string.
#Time - O(n2) (if palindrome is checked first, then it will be  O(n2)*O(logn))

class Solution:
    def isPalindrome(self, s: str)-> str:
        i,j=0,len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        i,j,result=0,0,''
        while i<=j and j<=len(s):
            string=s[i:j+1]
            if len(string)>len(result) and self.isPalindrome(string):
                result=string
            j+=1
            if j==len(s):
                i+=1
                j=i
        return result
s=input('Enter string to find longest palindromic substring /n')
longestPalindromeSubString=Solution()
print(longestPalindromeSubString.longestPalindrome(s))