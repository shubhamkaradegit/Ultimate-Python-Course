class Employee:
    a =1

    @classmethod   #this is decorator
    def show(cls):
        print(f"The class attribute of a is {cls.a}")   #self matlab jo object uspar method chal raha hai
                                                        #cls matalab jo class jiska object hai uspar method chal raha hai


# concept of incapsulation and abstraction

# incapsulation ka matlab hai ki aap ko nahi dikh raha hai ki implementation details kya hai
# abstraction ka matlab hai ki implementation details ko chupa diya hai hamne user se


    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname,e.lname)
e.show()