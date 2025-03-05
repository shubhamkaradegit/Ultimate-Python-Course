class Employee:
    company = "ITC"
    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is your language {self.language}")
# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")


#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in language {self.language}")

class Programmer(Employee,Coder):
     company = "ITC Infotech"
     def showLanguage(self):
        print(f"The name is {self.name} and he is good in language {self.language}")

a = Employee()
b = Programmer()

print(a.company,b.company)
print(b.show("shubham",1500000))

b.showLanguage()
b.printLanguage()
