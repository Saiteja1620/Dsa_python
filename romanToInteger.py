s=input('Enter Roman Number:/n')
numbers={
        'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000
        }
result=0
i=0
while i<len(s)-1:
    if numbers[s[i]]>=numbers[s[i+1]]:
        result+=numbers[s[i]]
        i+=1
    else:
        result+=numbers[s[i+1]]-numbers[s[i]]
        i+=2
if i<len(s):
    result+=numbers[s[i:]]
print(f'Convertion of roman {s} is {result}')