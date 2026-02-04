num=int(input("Enter a number to conver to roman: /n"))
d={
            1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'
        }
nums=list(d.keys())
numbers=[]
counter=0
while num:
    numbers.append((num%10)*(10**counter))
    num//=10
    counter+=1
numbers=numbers[::-1]
print(numbers)
result=''
counter=0
for i in range(len(numbers)):
    temp=numbers[i]
    while temp>0:
        # print(temp, 'is greater than 0')
        if (temp-max(nums))>=0 and str(temp)[0] not in ('4','9'):
            result+=d[max(nums)]
            temp-=max(nums)
        elif (temp-max(nums))<0 and str(temp)[0] not in ('4','9'):
            # print('Entered less than condition and removing max number from the list')
            nums.remove(max(nums))

        elif str(temp)[0] in ('4','9'):
            maxi,mini=0,min(nums)
            for i in nums:
                if i//temp<=1:
                    maxi=i
            # print(temp,nums,maxi,mini)
            t,s=maxi,''
            s+=d[t]
            if t-temp in d:
                s=d[t-temp]+s
                nums.remove(t)
            temp=temp - t
            result+=s
        print(result)