class Employee:
    language = "py"    #this is class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def __init__(self,name,salary,language):    # dunder method which is automatically called
        self.name = name
        self.salary  = salary
        self.language = language
        print("I am creating an object.")


shubham = Employee("shubham",1300000,"Javascript")
# shubham.language = "Javascript"   #this is an instance attribute

print(shubham.name,shubham.salary,shubham.language)


# harry.getInfo()
# Employee.getInfo(shubham)
