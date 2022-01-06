class a:
    def m1(self):
        print("a in class a")
class b(a):
    def m2(self):
        print("b in class b")
    def m1(self):
        print("b in class a")
obj=b()
obj.m2()
obj.m1()
