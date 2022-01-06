x=int(input("enter value "))
sum=0
for i in range(1,x):
    if x%i==0:
        sum=sum+i
if sum==x:
    print(x,"Perfect Number")
else:
    print(x,"Not Perfect Number")
        