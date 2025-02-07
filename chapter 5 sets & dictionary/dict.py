dic = {} #empty dictionary
marks = {
    "harry": 56,
    "shubham": 45,
    "rohan": 78,
}

print(marks, type(marks))

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"harry": 55, "renuka": 44})
print(marks)

#difference between get and [] syntax in dictionary
print(marks.get("harry2"))  #prints none
print(marks["harry2"]) #this will give an error



