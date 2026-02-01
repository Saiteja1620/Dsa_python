n=int(input('Enter any number to calculate number of trailing zeros'))
result=0
x=1
while 5**x<=n:
    result+=n//(5**x)
    x+=1
print(f'Number of trailing zeros in {n} factorial is ',result)