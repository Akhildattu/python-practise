# using nested if loop

x=int(input("Enter value "))
y=int(input("Enter value "))
z=int(input("Enter value "))
if x>y and x>z:
    print(x,"is greater")
elif y>x and y>z:
    print(y,"is greater")
else:
    print(z,"is greater")