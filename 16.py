x=int(input("Enter value "))
temp=x
rev=0
while x!=0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
if temp==rev:
    print("Palindrome")
    