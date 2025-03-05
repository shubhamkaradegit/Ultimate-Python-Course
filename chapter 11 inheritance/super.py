class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2


class Managaer(Programmer):
    def __init__(self):
        super().__init__()              #run the constructor of super class
        print("Constructor of Manager")
    c = 3

# o = Employee()
# p = Programmer()
m = Managaer()
# print(o.a)
# print(p.a ,p.b)
print(m.a,m.b,m.c)