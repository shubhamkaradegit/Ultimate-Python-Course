class Employee:
    a = 1

class Programmer(Employee):
    b = 2


class Managaer(Programmer):
    c = 3

o = Employee()
p = Programmer()
m = Managaer()
print(o.a)
print(p.a ,p.b)
print(m.a ,m.b,m.c)