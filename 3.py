# using for loop for even numbers and odd numbers
x=int(input("Enter value "))
print("Even Numbers")
for i in range(0,x+1):
    if i%2==0:
        print(i,end=" ")
print()
print("Odd Numbers")
for i in range(0,x+1):
    if i%2!=0:
        print(i,end=" ")