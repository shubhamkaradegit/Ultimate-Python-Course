class Employee:
    a =1

    @classmethod   #this is decorator
    def show(cls):
        print(f"The class attribute of a is {cls.a}")   #self matlab jo object uspar method chal raha hai
                                                        #cls matalab jo class jiska object hai uspar method chal raha hai

e = Employee()
e.a = 45
e.name = "shubham"
print(e.name)
e.show()
