class student:
    def __init__(self):
        self.name=input("Enter ")
        self.id=int(input("enter "))
    def display(self):
        print(self.name,self.id)
obj=student()
obj.display()