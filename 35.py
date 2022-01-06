def fib(x,y):
    for i in range(1,11):
        z=x+y
        print(z)
        x=y
        y=z
fib(0,1)