class Employee:
    language = "py"    #this is class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning!!")

    @staticmethod #if we don't have to use self we use @staticmethod because we are not taking language and salary.
    def greed():
        print("Good morning!!")


shubham = Employee()
shubham.language = "Javascript"   #this is an instance attribute


# harry.getInfo()
Employee.getInfo(shubham)
shubham.greet()
shubham.greed()