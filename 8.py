#using for loop
x=int(input("Enter value "))
fact=1
print(x,"Factorial ")
if x<=0:
    print("Cant Find")
else:
    for i in range(1,x+1):
        fact=fact*i
print(fact)