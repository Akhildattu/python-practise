x=input("Enter string ")
count=1
y=x.split(" ")
for i in range(len(y)):
    for j in range(i+1,len(y)):
        if y[i]==y[j]:
            count=count+1
    if count>1:
        print(y[i],count)
    count=1