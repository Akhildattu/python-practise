x=int(input("enter number "))
count=0
for i in range(2,x):
    if x%i==0:
        count=count+1
        break
if count==0:
    print("prime")
else:
    print("not prime")