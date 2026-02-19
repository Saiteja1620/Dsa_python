##Intution
#Two pointer
#i,j will refer to starting character of the string. j will start from i to length of the string.
# if i and j are equal and s[i] is not visited, then its a new element, consider and move the j forward. incase if it is visited, break the loop.
# if i and j are not equal and s[i] is equal to s[j] then, same element appeared twice, add it to visited , skip the combination of strings with the character at i. Move the i (break the inner loop)
# else it is a not visited string, we consider its length and store it to compare with rest.

##Complexity
#Time Complexity
#Worst Case O(n2) - all the elements are unique

#Space Complexity
#Wost Case - O(n) - we might need to store all the elements of that string if characters are unique.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>1:
            m=0
            for i in range(len(s)):
                visited=[]
                substring=''
                for j in range(i,len(s)):
                    if s[i]==s[j]:
                        if i==j:
                            if s[j] not in visited:
                                visited.append(s[i])
                                substring=s[i]
                        else:
                            if s[j] in visited:
                                visited.remove(s[i])
                                break
                    else:
                        if s[j] not in visited:
                            substring=s[i:j+1]
                            visited.append(s[j])
                        else:
                            visited.remove(s[j])
                            break
                if len(substring)>m:
                    m=len(substring)
            print('Max length of the substring without repeating characters is', m)
            exit(0)
        print('Input string length is less than one, input itself is the longest substring without repeating characters',len(s))
s=input('Enter any string to find longest substring without repeating characters \n')
ll=Solution()
ll.lengthOfLongestSubstring(s)