x=10
y=100
for i in range(0,5):
    if (i%2==0):
        for j in range(0,5):
            x=x+1
            print(x,end=' ')
    elif i%2!=0:
        for j in range(0,5):
            y=y-1
            print(y,end=" ")
    print()