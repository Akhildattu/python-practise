#using for loop
x=int(input("Enter table "))
a=0
z=1
for k in range(1,101):
    for j in range(1,11):
        y=x*j
        print(x,"*",j,"=",y)
    print()
    z=int(input("press for continue 1 or exit for 0 "))
    x=x+z
    if z==0:
        print("Exit")
        break

    
    