x=input("Enter string ")
a=b=c=d=0
for i in x:
    if i>='a' and i<='z':
        a=a+1
    elif i>='A' and i<='Z':
        b=b+1
    elif i>='0' and i<='9':
        c=c+1
    elif i!=" ":
        d=d+1
print("Upper case ",b)
print("Lower case ",a)
print("Number ",c)
print("Special character ",d)