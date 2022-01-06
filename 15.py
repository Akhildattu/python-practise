x=int(input("Enter value "))
i=1
p=1
while x!=0:
    rem=x%10
    p=p*rem
    x=x//10
print("p",p)
    