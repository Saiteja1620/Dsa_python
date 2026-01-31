#find the element that appears only once in an array where every other element appears twice
#method 1: using dictionary to count occurrences
# array=list(map(int,input().split()))
# d={}
# for i in array:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# for i in d:
#     if d[i]==1:
#         print(i)

#method 2: using XOR operation
array=list(map(int,input().split()))
result=0
for i in array:
    result^=i
print(result)
