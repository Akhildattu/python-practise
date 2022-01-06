x=int(input("enter value "))
y=len(str(x))
sum=0
temp=x
while x!=0:
    rem=x%10
    sum=sum+rem**y
    x=x//10
if temp==sum:
    print("Amstrong")
else:
    print("Not Amstrong")