x=[]
y=int(input("enter element "))
for i in range(0,y):
    z=int(input())
    x.append(z)
print("list elements ",x)
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)