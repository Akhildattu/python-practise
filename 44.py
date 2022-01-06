
import numpy as n
l=[]
x=int(input("Enter element "))
for i in range(0,x):
    y=int(input())
    l.append(y)
z=n.array(l)
print("Array elements ",z)
print("copy")
print(z.copy())
print("view")
print(z.view())