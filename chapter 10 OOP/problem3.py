class Demo:
    a = 4

o = Demo()
print(o.a)
o.a = 0
print(o.a)
print(Demo.a) #it dosen't change class attribute