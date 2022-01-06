def sumofdigits(x):
    sum=0
    while x!=0:
        rem=x%10
        sum=sum+rem
        x=x//10
    print(sum)  
sumofdigits(int(input("Enter value ")))
