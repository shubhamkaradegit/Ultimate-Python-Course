class Employee:
    language = "py"    #this is class attribute
    salary = 1200000


shubham = Employee()
shubham.language = "javascript"   #this is an instance attribute
print(shubham.language,shubham.salary)

#instance attribute take preference over the class attribute during assignment and retrival
