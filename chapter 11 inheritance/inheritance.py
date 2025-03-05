class Employee:
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")


#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in language {self.language}")

class Programmer(Employee):
     company = "ITC Infotech"
     def showLanguage(self):
        print(f"The name is {self.name} and he is good in language {self.language}")

a = Employee()
b = Programmer()

print(a.company,b.company)
print(b.show("shubham",1500000))
