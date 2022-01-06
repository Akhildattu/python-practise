x=int(input("Enter value "))
sum=0
count=0
while x!=0:
    rem=x%10
    sum=sum+rem
    x=x//10
    count=count+1
print("sum",sum)
print("Count",count)